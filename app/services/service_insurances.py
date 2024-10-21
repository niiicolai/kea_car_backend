from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.insurance import Insurance
from sqlalchemy.orm import Session
from typing import List, cast

def get_all(session: Session) -> List[Insurance]:
    insurances = session.query(Insurance).all()
    return cast(List[Insurance], insurances)