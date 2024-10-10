from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.customer import Customer
from app.resources.customer_resource import CustomerCreateResource
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[Customer]:
    customers = session.query(Customer).all()
    return cast(list[Customer], customers)


def get_by_id(session: Session, customer_id: int) -> Customer:
    customer: Customer = session.query(Customer).get(customer_id)
    if customer is None:
        raise UnableToFindIdError(entity_name="Customer", entity_id=customer_id)
    return customer


def create(session: Session, customer_data: CustomerCreateResource) -> Customer:
    new_customer = Customer(
        email=customer_data.email,
        phone_number=customer_data.phone_number,
        first_name=customer_data.first_name,
        last_name=customer_data.last_name,
        address=customer_data.address,
    )
    session.add(new_customer)
    session.commit()
    session.refresh(new_customer)
    return new_customer