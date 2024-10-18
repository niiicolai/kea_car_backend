from abc import ABC, abstractmethod
from typing import Optional, Tuple
from app.resources.sales_person_resource import SalesPersonReturnResource
from app.models.sales_person import SalesPerson
from sqlalchemy.orm import Session


class SalesPersonRepository(ABC):
    @abstractmethod
    def fetch_by_email(self, email: str) -> Tuple[Optional[SalesPersonReturnResource], Optional[str]]:
        pass


class MySQLSalesPersonRepository(SalesPersonRepository):
    def __init__(self, session: Session):
        self.session = session

    def fetch_by_email(self, email: str) -> Tuple[Optional[SalesPersonReturnResource], Optional[str]]:
        sales_person: Optional[SalesPerson] = self.session.query(SalesPerson).filter_by(email=email).first()

        if sales_person is not None:
            sales_person_resource: SalesPersonReturnResource = sales_person.as_resource()
            hashed_password: str = sales_person.password
            return sales_person_resource, hashed_password
        return None, None


# Placeholder for future repositories
# class OtherDBSalesPersonRepository(SalesPersonRepository):
#     ...