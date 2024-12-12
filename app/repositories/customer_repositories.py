# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, Union, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database
from neo4j import Session as Neo4jSession, Query

# Internal library imports
from app.models.customer import (
    CustomerReturnResource,
    CustomerMySQLEntity,
    CustomerMongoEntity,
    CustomerNeo4jEntity
)
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource


class CustomerRepository(ABC):

    @abstractmethod
    def get_all(
            self,
            email_filter: Optional[str] = None,
            limit: Optional[int] = None
    ) -> List[CustomerReturnResource]:  # pragma: no cover
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[CustomerReturnResource]:  # pragma: no cover
        pass

    @abstractmethod
    def create(self, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:  # pragma: no cover
        pass

    @abstractmethod
    def update(
            self,
            customer_id: str,
            customer_update_data: CustomerUpdateResource
    ) -> Optional[CustomerReturnResource]:  # pragma: no cover
        pass

    @abstractmethod
    def delete(self, customer_resource: CustomerReturnResource):  # pragma: no cover
        pass

    @abstractmethod
    def is_email_taken(
            self,
            customer_resource: Union[CustomerUpdateResource,
            CustomerCreateResource],
            customer_id: Optional[str] = None
    ) -> bool:  # pragma: no cover
        pass


class MySQLCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(
            self,
            email_filter: Optional[str] = None,
            limit: Optional[int] = None
    ) -> List[CustomerReturnResource]:

        customers_query = self.session.query(CustomerMySQLEntity)
        if email_filter is not None and isinstance(email_filter, str):
            customers_query = customers_query.filter(CustomerMySQLEntity.email.contains(email_filter))
        if limit is not None and isinstance(limit, int) and limit > 0:
            customers_query = customers_query.limit(limit)
        customers: List[CustomerMySQLEntity] = cast(List[CustomerMySQLEntity], customers_query.all())
        return [customer.as_resource() for customer in customers]

    def get_by_id(
            self,
            customer_id: str
    ) -> Optional[CustomerReturnResource]:

        customer: Optional[CustomerMySQLEntity] = self.session.get(CustomerMySQLEntity, customer_id)
        if customer is not None:
            return customer.as_resource()
        return None

    def create(
            self,
            customer_create_data: CustomerCreateResource
    ) -> CustomerReturnResource:

        new_customer = CustomerMySQLEntity(
            email=customer_create_data.email,
            phone_number=customer_create_data.phone_number,
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            address=customer_create_data.address,
        )
        self.session.add(new_customer)
        self.session.flush()
        self.session.refresh(new_customer)

        return new_customer.as_resource()

    def update(
            self,
            customer_id: str,
            customer_update_data: CustomerUpdateResource
    ) -> Optional[CustomerReturnResource]:

        customer: Optional[CustomerMySQLEntity] = self.session.get(CustomerMySQLEntity, customer_id)
        if customer is None:
            return None

        for key, value in customer_update_data.get_updated_fields().items():
            setattr(customer, key, value)

        self.session.flush()
        self.session.refresh(customer)

        return customer.as_resource()

    def delete(
            self,
            customer_resource: CustomerReturnResource
    ) -> None:
        self.session.query(CustomerMySQLEntity).filter_by(id=customer_resource.id).delete(
            synchronize_session=False
        )
        self.session.flush()

    def is_email_taken(
            self,
            customer_resource: Union[CustomerUpdateResource, CustomerCreateResource],
            customer_id: Optional[str] = None
    ) -> bool:
        email_query = self.session.query(CustomerMySQLEntity.id).filter_by(email=customer_resource.email)
        if customer_id is not None:
            email_query = email_query.filter(customer_id != CustomerMySQLEntity.id)
        return self.session.query(email_query.exists()).scalar()


class MongoDBCustomerRepository(CustomerRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database

    def get_all(
            self,
            email_filter: Optional[str] = None,
            limit: Optional[int] = None
    ) -> List[CustomerReturnResource]:
        query = {}
        if email_filter is not None and isinstance(email_filter, str):
            query["email"] = {"$regex": email_filter}
        customers_cursor = self.database.get_collection("customers").find(query).limit(0 if not limit else limit)
        customers = [
            CustomerMongoEntity(**customer).as_resource()
            for customer in customers_cursor
        ]
        return customers

    def get_by_id(
            self,
            customer_id: str
    ) -> Optional[CustomerReturnResource]:
        customer = self.database.get_collection("customers").find_one({"_id": customer_id})
        if customer is not None:
            return CustomerMongoEntity(**customer).as_resource()
        return None

    def create(
            self,
            customer_create_data: CustomerCreateResource
    ) -> CustomerReturnResource:
        new_customer = CustomerMongoEntity(
            email=customer_create_data.email,
            phone_number=customer_create_data.phone_number,
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            address=customer_create_data.address,
        )
        self.database.get_collection("customers").insert_one(new_customer.model_dump(by_alias=True))
        return new_customer.as_resource()

    def update(
            self,
            customer_id: str,
            customer_update_data: CustomerUpdateResource
    ) -> Optional[CustomerReturnResource]:
        updated_customer = self.database.get_collection("customers").find_one_and_update(
            {"_id": customer_id},
            {"$set": customer_update_data.get_updated_fields()},
            return_document=True
        )
        if updated_customer is not None:
            self.database.get_collection("cars").update_many(
                {"customer._id": customer_id},
                {"$set": {"customer": updated_customer}}
            )
            self.database.get_collection("purchases").update_many(
                {"car.customer._id": customer_id},
                {"$set": {"car.customer": updated_customer}}
            )
            return CustomerMongoEntity(**updated_customer).as_resource()
        return None

    def delete(
            self,
            customer_resource: CustomerReturnResource
    ) -> None:
        self.database.get_collection("cars").delete_many({"customer._id": customer_resource.id})
        self.database.get_collection("purchases").delete_many({"car.customer._id": customer_resource.id})
        self.database.get_collection("customers").delete_one({"_id": customer_resource.id})

    def is_email_taken(
            self,
            customer_resource: Union[CustomerUpdateResource, CustomerCreateResource],
            customer_id: Optional[str] = None
    ) -> bool:
        email_query = {"email": customer_resource.email}
        if customer_id is not None:
            email_query["_id"] = {"$ne": customer_id}
        return self.database.get_collection("customers").count_documents(email_query) > 0



class Neo4jCustomerRepository(CustomerRepository):  # pragma: no cover
    def __init__(self, session: Neo4jSession):
        self.session = session

    def get_all(
            self,
            email_filter: Optional[str] = None,
            limit: Optional[int] = None
    ) -> List[CustomerReturnResource]:
        query = "MATCH (c:Customer) "
        if email_filter is not None and isinstance(email_filter, str):
            query += f"WHERE c.email CONTAINS '{email_filter}' "
        query += "RETURN c"
        if limit is not None and isinstance(limit, int) and limit > 0:
            query += f" LIMIT {limit}"
        result = self.session.run(query)
        customers = [record["c"] for record in result]
        return [CustomerNeo4jEntity(**customer).as_resource() for customer in customers]

    def get_by_id(
            self,
            customer_id: str
    ) -> Optional[CustomerReturnResource]:
        query = f"MATCH (c:Customer {{id: '{customer_id}'}}) RETURN c"
        result = self.session.run(query)
        customer = result.single()
        if customer is not None:
            return CustomerNeo4jEntity(**customer["c"]).as_resource()
        return None

    def create(
            self,
            customer_create_data: CustomerCreateResource
    ) -> CustomerReturnResource:
        new_customer = CustomerNeo4jEntity(
            email=customer_create_data.email,
            phone_number=customer_create_data.phone_number,
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            address=customer_create_data.address,
        )
        query = Query("CREATE (c:Customer $customer_creat_data) RETURN c")
        result = self.session.run(query, customer_creat_data=new_customer.model_dump())
        created_customer = result.single()
        return CustomerNeo4jEntity(**created_customer["c"]).as_resource()

    def update(
            self,
            customer_id: str,
            customer_update_data: CustomerUpdateResource
    ) -> Optional[CustomerReturnResource]:
        updated_fields = customer_update_data.get_updated_fields()
        set_clause = ", ".join([f"c.{key} = ${key}" for key in updated_fields.keys()])
        query = Query(f"MATCH (c:Customer {{id: $customer_id}}) SET {set_clause} RETURN c")
        parameters = {"customer_id": customer_id, **updated_fields}
        result = self.session.run(query, parameters)
        updated_customer = result.single()
        if updated_customer is not None:
            return CustomerNeo4jEntity(**updated_customer["c"]).as_resource()
        return None

    def delete(
            self,
            customer_resource: CustomerReturnResource
    ) -> None:
        query = Query("""
        MATCH (customer:Customer {id: $customer_id})
        OPTIONAL MATCH (car:Car)-[:OWNED_BY]->(customer)
        OPTIONAL MATCH (purchase:Purchase)-[:MADE_FOR]->(car)
        DETACH DELETE customer, car, purchase
        """)
        self.session.run(query, customer_id=customer_resource.id)

    def is_email_taken(
            self,
            customer_resource: Union[CustomerUpdateResource, CustomerCreateResource],
            customer_id: Optional[str] = None
    ) -> bool:
        query = f"MATCH (c:Customer {{email: '{customer_resource.email}'}})"
        if customer_id is not None:
            query += f" WHERE c.id <> '{customer_id}'"
        query += " RETURN c"
        result = self.session.run(query)
        return result.single() is not None
