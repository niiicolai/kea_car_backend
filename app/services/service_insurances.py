from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.insurance import Insurance
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[Insurance]:
    insurances = session.query(Insurance).all()
    return cast(list[Insurance], insurances)