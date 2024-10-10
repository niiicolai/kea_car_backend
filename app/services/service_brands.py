from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.brand import Brand
from sqlalchemy.orm import Session
from typing import cast

def get_all(session: Session) -> list[Brand]:
    brands = session.query(Brand).all()
    return cast(list[Brand], brands)