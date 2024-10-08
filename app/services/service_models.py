from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.model import Model
from sqlalchemy.orm import Session

def get_all(brand_id: int | None, session: Session) -> list[Model]:
    if brand_id is not None:
        models = session.query(Model).filter_by(brands_id = brand_id).all()
        if models.count == 0:
            raise UnableToFindIdError(entity_name="Brand", entity_id=brand_id)
        return models
    return session.query(Model).all()