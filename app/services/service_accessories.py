from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.accessory import Accessory
from sqlalchemy.orm import Session
from typing import List, cast

def get_all(session: Session) -> List[Accessory]:
    accessories = session.query(Accessory).all()
    return cast(List[Accessory], accessories)