# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.customer import CustomerReturnResource, CustomerMySQLEntity
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource


class CustomerRepository(ABC):

    @abstractmethod
    def get_all(self, limit: Optional[int]) -> List[CustomerReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[CustomerReturnResource]:
        pass

    @abstractmethod
    def create(self, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:
        pass

    @abstractmethod
    def update(self, customer_id: str, customer_update_data: CustomerUpdateResource) -> Optional[CustomerReturnResource]:
        pass

    @abstractmethod
    def delete(self, customer_id: str) -> Optional[CustomerReturnResource]:
        pass

    @abstractmethod
    def is_email_taken(self, email: str) -> bool:
        pass

class MySQLCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int]) -> List[CustomerReturnResource]:
        customers_query = self.session.query(CustomerMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            customers_query = customers_query.limit(limit)
        customers: List[CustomerMySQLEntity] = cast(List[CustomerMySQLEntity], customers_query.all())
        return [customer.as_resource() for customer in customers]

    def get_by_id(self, customer_id: str) -> Optional[CustomerReturnResource]:
        customer: Optional[CustomerMySQLEntity] = self.session.query(CustomerMySQLEntity).get(customer_id)
        if customer is not None:
            return customer.as_resource()
        return None

    def create(self, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:
        new_customer = CustomerMySQLEntity(
            email=customer_create_data.email,
            phone_number=customer_create_data.phone_number,
            first_name=customer_create_data.first_name,
            last_name=customer_create_data.last_name,
            address=customer_create_data.address,
        )
        self.session.add(new_customer)
        self.session.commit()
        self.session.refresh(new_customer)

        return new_customer.as_resource()

    def update(self, customer_id: str, customer_update_data: CustomerUpdateResource) -> Optional[CustomerReturnResource]:
        customer: Optional[CustomerMySQLEntity] = self.session.query(CustomerMySQLEntity).get(customer_id)
        if customer is None:
            return None

        for key, value in customer_update_data.get_updated_fields().items():
            setattr(customer, key, value)

        self.session.commit()
        self.session.refresh(customer)

        return customer.as_resource()

    def delete(self, customer_id: str) -> Optional[CustomerReturnResource]:
        customer: Optional[CustomerMySQLEntity] = self.session.query(CustomerMySQLEntity).get(customer_id)
        if customer is None:
            return None
        customer_resource = customer.as_resource()
        self.session.query(CustomerMySQLEntity).filter_by(id=customer_id).delete(
            synchronize_session=False
        )
        self.session.commit()
        return customer_resource

    def is_email_taken(self, email: str) -> bool:
        return self.session.query(CustomerMySQLEntity).filter_by(email=email).first() is not None

# Placeholder for future repositories
# class OtherDBCustomerRepository(CustomerRepository):
#     ...