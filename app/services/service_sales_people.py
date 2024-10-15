from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from pydantic import ValidationError
from app.models.sales_person import SalesPerson
from app.resources.sales_person_resource import SalesPersonLoginResource
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[SalesPerson]:
    sales_people = session.query(SalesPerson).all()
    return cast(list[SalesPerson], sales_people)


def login(sales_person_login_data: SalesPersonLoginResource, session: Session) -> SalesPerson:
    logged_in_sales_person = session.query(SalesPerson).filter_by(email=sales_person_login_data.email).first()
    if logged_in_sales_person is None:
        raise ValidationError(f"No Sales Person with the email: '{sales_person_login_data.email}'")
    if logged_in_sales_person.password != sales_person_login_data.password:
        raise ValidationError(f"Incorrect password for Sales Person with the email: '{logged_in_sales_person.email}'!")
    return cast(SalesPerson, logged_in_sales_person)