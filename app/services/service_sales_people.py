from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.sales_person import SalesPerson
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[SalesPerson]:
    sales_people = session.query(SalesPerson).all()
    return cast(list[SalesPerson], sales_people)