# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.core.security import Token, create_access_token, verify_password, get_password_hash
from app.exceptions.invalid_credentials_errors import IncorrectEmailError, IncorrectPasswordError
from app.repositories.sales_person_repositories import (
    SalesPersonRepository,
    SalesPersonReturnResource,
    SalesPersonCreateResource,
    SalesPersonLoginResource
)


def get_all(repository: SalesPersonRepository, sales_people_limit: Optional[int] = None) -> List[SalesPersonReturnResource]:
    if not isinstance(repository, SalesPersonRepository):
        raise TypeError(f"repository must be of type SalesPersonRepository, not {type(repository).__name__}.")
    if not (isinstance(sales_people_limit, int) or sales_people_limit is None):
        raise TypeError(f"sales_people_limit must be of type int or None, not {type(sales_people_limit).__name__}.")

    return repository.get_all(limit=sales_people_limit)

def get_by_id(repository: SalesPersonRepository, sales_person_id: str) -> SalesPersonReturnResource:
    if not isinstance(repository, SalesPersonRepository):
        raise TypeError(f"repository must be of type SalesPersonRepository, not {type(repository).__name__}.")
    if not isinstance(sales_person_id, str):
        raise TypeError(f"sales_person_id must be of type str, not {type(sales_person_id).__name__}.")

    sales_person = repository.get_by_id(sales_person_id)
    if sales_person is None:
        raise UnableToFindIdError(entity_name="Sales Person", entity_id=sales_person_id)
    return sales_person


def login(repository: SalesPersonRepository, sales_person_login_data: SalesPersonLoginResource) -> Token:
    if not isinstance(repository, SalesPersonRepository):
        raise TypeError(f"repository must be of type SalesPersonRepository, not {type(repository).__name__}.")
    if not isinstance(sales_person_login_data, SalesPersonLoginResource):
        raise TypeError(f"sales_person_login_data must be of type SalesPersonLoginResource, not {type(sales_person_login_data).__name__}.")

    verified_email = repository.login_by_email(sales_person_login_data)
    if verified_email is None:
        raise IncorrectEmailError(sales_person_login_data.email)

    sales_person_resource, hashed_password = verified_email
    if not verify_password(sales_person_login_data.password, hashed_password):
        raise IncorrectPasswordError(sales_person_resource.email, sales_person_login_data.password)

    return create_access_token(sales_person_resource)

def create(repository: SalesPersonRepository, sales_person_create_data: SalesPersonCreateResource) -> SalesPersonReturnResource:
    if not isinstance(repository, SalesPersonRepository):
        raise TypeError(f"repository must be of type SalesPersonRepository, not {type(repository).__name__}.")
    if not isinstance(sales_person_create_data, SalesPersonCreateResource):
        raise TypeError(f"sales_person_create_data must be of type SalesPersonCreateResource, not {type(sales_person_create_data).__name__}.")

    hashed_password: str = get_password_hash(sales_person_create_data.password)
    if repository.is_email_taken(sales_person_create_data.email):
        raise AlreadyTakenFieldValueError(
            entity_name="Sales Person",
            field="email",
            value=sales_person_create_data.email
        )
    return repository.create(sales_person_create_data, hashed_password)

