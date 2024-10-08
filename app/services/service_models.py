from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.model import Model
from app.models.brand import Brand
from sqlalchemy.orm import Session

def get_all(brand_id: int | None, session: Session) -> list[Model]:
    if brand_id is not None:
        if session.query(Brand).get(brand_id) is None:
            raise UnableToFindIdError(entity_name="Brand", entity_id=brand_id)
        return session.query(Model).filter_by(brands_id = brand_id).all()
    return session.query(Model).all()