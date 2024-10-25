from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.customer_repositories import CustomerRepository, CustomerReturnResource, CustomerCreateResource
from typing import List

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