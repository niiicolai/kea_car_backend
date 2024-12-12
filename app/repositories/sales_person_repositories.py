# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, Tuple, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database

# Internal library imports
from app.models.sales_person import (
    SalesPersonReturnResource,
    SalesPersonMySQLEntity,
    SalesPersonMongoEntity,
)
from app.resources.sales_person_resource import SalesPersonCreateResource, SalesPersonLoginResource


class SalesPersonRepository(ABC):  # pragma: no cover
    @abstractmethod
    def login_by_email(
            self,
            sales_person_login_info: SalesPersonLoginResource
    ) -> Optional[Tuple[SalesPersonReturnResource, str]]:
        pass

    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[SalesPersonReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, sales_person_id: str) -> Optional[SalesPersonReturnResource]:
        pass

    @abstractmethod
    def create(
            self,
            sales_person_create_data: SalesPersonCreateResource,
            hashed_password: str
    ) -> SalesPersonReturnResource:
        pass

    @abstractmethod
    def is_email_taken(self, email: str) -> bool:
        pass


class MySQLSalesPersonRepository(SalesPersonRepository):
    def __init__(self, session: Session):
        self.session = session

    def login_by_email(
            self,
            sales_person_login_info: SalesPersonLoginResource
    ) -> Optional[Tuple[SalesPersonReturnResource, str]]:

        sales_person_query = self.session.query(SalesPersonMySQLEntity).filter_by(email=sales_person_login_info.email)
        sales_person: Optional[SalesPersonMySQLEntity] = sales_person_query.first()

        if sales_person is None:
            return None

        sales_person_resource: SalesPersonReturnResource = sales_person.as_resource()
        hashed_password: str = sales_person.hashed_password
        return sales_person_resource, hashed_password

    def get_all(self, limit: Optional[int] = None) -> List[SalesPersonReturnResource]:
        sales_people_query = self.session.query(SalesPersonMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            sales_people_query = sales_people_query.limit(limit)
        sales_people: List[SalesPersonMySQLEntity] = cast(List[SalesPersonMySQLEntity], sales_people_query.all())
        return [sales_person.as_resource() for sales_person in sales_people]

    def get_by_id(self, sales_person_id: str) -> Optional[SalesPersonReturnResource]:
        sales_person: Optional[SalesPersonMySQLEntity] = self.session.get(SalesPersonMySQLEntity, sales_person_id)
        if sales_person is None:
            return None

        return sales_person.as_resource()

    def create(
            self,
            sales_person_create_data: SalesPersonCreateResource,
            hashed_password: str
    ) -> SalesPersonReturnResource:

        new_sales_person = SalesPersonMySQLEntity(
            email=sales_person_create_data.email,
            hashed_password=hashed_password,
            first_name=sales_person_create_data.first_name,
            last_name=sales_person_create_data.last_name,
        )
        self.session.add(new_sales_person)
        self.session.flush()
        self.session.refresh(new_sales_person)

        return new_sales_person.as_resource()

    def is_email_taken(self, email: str) -> bool:
        return (
            self.session.query(
                self.session.query(SalesPersonMySQLEntity.id)
                .filter_by(email=email).exists()
            ).scalar()
        )


class MongoDBSalesPersonRepository(SalesPersonRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database

    def login_by_email(
            self,
            sales_person_login_info: SalesPersonLoginResource
    ) -> Optional[Tuple[SalesPersonReturnResource, str]]:

        sales_person_query = self.database.get_collection("sales_people").find_one(
            {"email": sales_person_login_info.email}
        )
        if sales_person_query is not None:
            hashed_password = sales_person_query.get("hashed_password")
            sales_person = SalesPersonMongoEntity(**sales_person_query)
            return sales_person.as_resource(), hashed_password
        return None


    def get_all(self, limit: Optional[int] = None) -> List[SalesPersonReturnResource]:
        sales_people_query = self.database.get_collection("sales_people").find()
        if limit is not None and isinstance(limit, int) and limit > 0:
            sales_people_query = sales_people_query.limit(limit)
        sales_people = [SalesPersonMongoEntity(**sales_person).as_resource() for sales_person in sales_people_query]
        return sales_people

    def get_by_id(self, sales_person_id: str) -> Optional[SalesPersonReturnResource]:
        sales_person_query = self.database.get_collection("sales_people").find_one({"_id": sales_person_id})
        if sales_person_query is None:
            return None

        return SalesPersonMongoEntity(**sales_person_query).as_resource()

    def create(
            self,
            sales_person_create_data: SalesPersonCreateResource,
            hashed_password: str
    ) -> SalesPersonReturnResource:

        new_sales_person = SalesPersonMongoEntity(
            **sales_person_create_data.model_dump(exclude={"password"}),
            hashed_password=hashed_password
        )
        self.database.sales_people.insert_one(new_sales_person.model_dump(by_alias=True))
        return new_sales_person.as_resource()

    def is_email_taken(self, email: str) -> bool:
        return self.database.get_collection("sales_people").count_documents({"email": email}) > 0



# Placeholder for future repositories
# class OtherDBSalesPersonRepository(SalesPersonRepository):
#     ...
