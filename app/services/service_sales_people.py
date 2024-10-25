# External Library imports
from typing import List

# Internal library imports
from app.resources.sales_person_resource import SalesPersonLoginResource
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.exceptions.invalid_credentials_errors import IncorrectEmailError, IncorrectPasswordError
from app.core.security import Token, create_access_token, verify_password, get_password_hash
from app.repositories.sales_person_repositories import SalesPersonRepository, SalesPersonReturnResource, SalesPersonCreateResource


def get_all(repository: SalesPersonRepository) -> List[SalesPersonReturnResource]:
    return repository.get_all()

def get_by_id(repository: SalesPersonRepository, sales_person_id: str) -> SalesPersonReturnResource:
    sales_person = repository.get_by_id(sales_person_id)
    if sales_person is None:
        raise UnableToFindIdError(entity_name="Sales Person", entity_id=sales_person_id)
    return sales_person


def login(repository: SalesPersonRepository, sales_person_login_data: SalesPersonLoginResource) -> Token:
    verified_email = repository.fetch_by_email(sales_person_login_data.email)
    if verified_email is None:
        raise IncorrectEmailError(sales_person_login_data.email)

    sales_person_resource, hashed_password = verified_email
    if not verify_password(sales_person_login_data.password, hashed_password):
        raise IncorrectPasswordError(sales_person_resource.email, sales_person_login_data.password)

    return create_access_token(sales_person_resource)

def create(repository: SalesPersonRepository, sales_person_create_data: SalesPersonCreateResource) -> SalesPersonReturnResource:
    hashed_password: str = get_password_hash(sales_person_create_data.password)
    if repository.is_email_taken(sales_person_create_data.email):
        raise AlreadyTakenFieldValueError(
            entity_name="Sales Person",
            field="email",
            value=sales_person_create_data.email
        )
    return repository.create(sales_person_create_data, hashed_password)