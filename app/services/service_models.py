from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.model import Model
from app.models.brand import Brand
from sqlalchemy.orm import Session
from typing import List, Optional, cast

def get_all(brand_id: Optional[str], session: Session) -> List[Model]:
    if brand_id is not None:
        if session.query(Brand).get(brand_id) is None:
            raise UnableToFindIdError(entity_name="Brand", entity_id=brand_id)
        models = session.query(Model).filter_by(brands_id = brand_id).all()
    else:
        models = session.query(Model).all()
    return cast(List[Model], models)