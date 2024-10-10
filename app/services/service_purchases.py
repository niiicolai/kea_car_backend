from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.purchase import Purchase
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[Purchase]:
    purchases = session.query(Purchase).all()
    return cast(list[Purchase], purchases)