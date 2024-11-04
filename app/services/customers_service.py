# External Library imports
from typing import List

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.customer_repositories import (
    CustomerRepository,
    CustomerReturnResource,
    CustomerCreateResource,
    CustomerUpdateResource
)


def get_all(repository: CustomerRepository) -> List[CustomerReturnResource]:
    return repository.get_all()


def get_by_id(repository: CustomerRepository, customer_id: str) -> CustomerReturnResource:
    customer = repository.get_by_id(customer_id)
    if customer is None:
        raise UnableToFindIdError(entity_name="Customer", entity_id=customer_id)
    return customer


def create(repository: CustomerRepository, customer_create_data: CustomerCreateResource) -> CustomerReturnResource:
    if repository.is_email_taken(customer_create_data.email):
        raise AlreadyTakenFieldValueError(entity_name="Customer", field="email", value=customer_create_data.email)
    return repository.create(customer_create_data)

def update(repository: CustomerRepository, customer_id: str, customer_update_data: CustomerUpdateResource) -> CustomerReturnResource:
    if customer_update_data.email is not None and repository.is_email_taken(customer_update_data.email):
        raise AlreadyTakenFieldValueError(entity_name="Customer", field="email", value=customer_update_data.email)

    updated_customer = repository.update(customer_id, customer_update_data)
    if updated_customer is None:
        raise UnableToFindIdError(entity_name="Customer", entity_id=customer_id)

    return updated_customer

def delete(repository: CustomerRepository, customer_id: str) -> CustomerReturnResource:
    customer_resourcer = repository.delete(customer_id)
    if customer_resourcer is None:
        raise UnableToFindIdError(entity_name="Customer", entity_id=customer_id)
    return customer_resourcer
