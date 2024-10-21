from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from pydantic import ValidationError
from app.models.sales_person import SalesPerson
from app.resources.sales_person_resource import SalesPersonLoginResource, SalesPersonCreateResource
from app.core.security import get_password_hash
from sqlalchemy.orm import Session
from typing import List, Optional, cast
from app.core.security import verify_password

def get_all(session: Session) -> List[SalesPerson]:
    sales_people = session.query(SalesPerson).all()
    return cast(List[SalesPerson], sales_people)


def login(sales_person_login_data: SalesPersonLoginResource, session: Session) -> SalesPerson:
    sales_person = session.query(SalesPerson).filter_by(email=sales_person_login_data.email).first()
    if sales_person is None:
        raise ValidationError(f"No Sales Person with the email: '{sales_person_login_data.email}'")
    sales_person = cast(SalesPerson, sales_person)
    hashed_password = sales_person.hashed_password
    if not verify_password(sales_person_login_data, hashed_password):
        raise ValidationError(f"Incorrect password for Sales Person with the email: '{sales_person.email}'!")
    return sales_person

def create(sales_person_create_data: SalesPersonCreateResource, session: Session) -> SalesPerson:
    hashed_password = get_password_hash(sales_person_create_data.password)

    new_sales_person = SalesPerson(
        email=sales_person_create_data.email,
        hashed_password=hashed_password,
        first_name=sales_person_create_data.first_name,
        last_name=sales_person_create_data.last_name,
    )
    session.add(new_sales_person)
    session.commit()
    session.refresh(new_sales_person)
    return new_sales_person