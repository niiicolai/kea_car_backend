# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.customer_repositories import (
    CustomerRepository,
    CustomerReturnResource,
    CustomerCreateResource,
    CustomerUpdateResource
)


def get_all(
        repository: CustomerRepository,
        filter_customer_by_email: Optional[str] = None,
        customers_limit: Optional[int] = None,
        customers_page: int = 1
) -> List[CustomerReturnResource]:

    if not isinstance(repository, CustomerRepository):
        raise TypeError(f"repository must be of type CustomerRepository, "
                        f"not {type(repository).__name__}.")
    if not (isinstance(filter_customer_by_email, str) or filter_customer_by_email is None):
        raise TypeError(f"filter_customer_by_email must be of type str or None, "
                        f"not {type(filter_customer_by_email).__name__}.")
    if isinstance(customers_limit, bool) or not (isinstance(customers_limit, int) or customers_limit is None):
        raise TypeError(f"customers_limit must be of type int or None, "
                        f"not {type(customers_limit).__name__}.")
    if isinstance(customers_page, bool) or not isinstance(customers_page, int):
        raise TypeError(f"customers_page must be of type int, "
                        f"not {type(customers_page).__name__}.")
    return repository.get_all(
        email_filter=filter_customer_by_email,
        limit=customers_limit,
        page=customers_page
    )


def get_by_id(
        repository: CustomerRepository,
        customer_id: str
) -> CustomerReturnResource:

    if not isinstance(repository, CustomerRepository):
        raise TypeError(f"repository must be of type CustomerRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(customer_id, str):
        raise TypeError(f"customer_id must be of type str, "
                        f"not {type(customer_id).__name__}.")

    customer = repository.get_by_id(customer_id)
    if customer is None:
        raise UnableToFindIdError(
            entity_name="Customer",
            entity_id=customer_id
        )
    return customer


def create(
        repository: CustomerRepository,
        customer_create_data: CustomerCreateResource
) -> CustomerReturnResource:

    if not isinstance(repository, CustomerRepository):
        raise TypeError(f"repository must be of type CustomerRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(customer_create_data, CustomerCreateResource):
        raise TypeError(f"customer_create_data must be of type CustomerCreateResource, "
                        f"not {type(customer_create_data).__name__}.")

    if repository.is_email_taken(customer_create_data):
        raise AlreadyTakenFieldValueError(
            entity_name="Customer",
            field="email",
            value=customer_create_data.email
        )

    return repository.create(customer_create_data)

def update(
        repository: CustomerRepository,
        customer_id: str,
        customer_update_data: CustomerUpdateResource
) -> CustomerReturnResource:

    if not isinstance(repository, CustomerRepository):
        raise TypeError(f"repository must be of type CustomerRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(customer_id, str):
        raise TypeError(f"customer_id must be of type str, "
                        f"not {type(customer_id).__name__}.")
    if not isinstance(customer_update_data, CustomerUpdateResource):
        raise TypeError(f"customer_update_data must be of type CustomerUpdateResource, "
                        f"not {type(customer_update_data).__name__}.")

    if customer_update_data.email is not None and repository.is_email_taken(customer_update_data, customer_id):
        raise AlreadyTakenFieldValueError(
            entity_name="Customer",
            field="email",
            value=customer_update_data.email
        )

    updated_customer = repository.update(customer_id, customer_update_data)
    if updated_customer is None:
        raise UnableToFindIdError(
            entity_name="Customer",
            entity_id=customer_id
        )

    return updated_customer

def delete(
        repository: CustomerRepository,
        customer_id: str
) -> None:

    if not isinstance(repository, CustomerRepository):
        raise TypeError(f"repository must be of type CustomerRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(customer_id, str):
        raise TypeError(f"customer_id must be of type str, "
                        f"not {type(customer_id).__name__}.")

    customer_resource = repository.get_by_id(customer_id)
    if customer_resource is None:
        raise UnableToFindIdError(
            entity_name="Customer",
            entity_id=customer_id
        )
    repository.delete(customer_resource)
