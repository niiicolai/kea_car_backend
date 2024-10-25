from abc import ABC, abstractmethod
from typing import Optional, List, cast
from app.resources.customer_resource import CustomerReturnResource, CustomerCreateResource
from app.models.customer import Customer
from sqlalchemy.orm import Session


class CustomerRepository(ABC):


    @abstractmethod
    def get_all(self) -> List[CustomerReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[CustomerReturnResource]:
        pass

    @abstractmethod
    def create(self, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:
        pass

    @abstractmethod
    def is_email_taken(self, email: str) -> bool:
        pass

class MySQLCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[CustomerReturnResource]:
        customers: List[Customer] = cast(List[Customer], self.session.query(Customer).all())
        return [customer.as_resource() for customer in customers]

    def get_by_id(self, customer_id: str) -> Optional[CustomerReturnResource]:
        customer: Optional[Customer] = self.session.query(Customer).get(customer_id)
        if customer is not None:
            return customer.as_resource()
        return None

    def create(self, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:
        new_customer = Customer(
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

    def is_email_taken(self, email: str) -> bool:
        return self.session.query(Customer).filter_by(email=email).first() is not None

# Placeholder for future repositories
# class OtherDBCustomerRepository(CustomerRepository):
#     ...