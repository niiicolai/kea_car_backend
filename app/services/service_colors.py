from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.color import Color
from app.resources.color_resource import ColorCreateResource
from sqlalchemy.orm import Session
from typing import List, cast

def get_all(session: Session) -> List[Color]:
    colors = session.query(Color).all()
    return cast(List[Color], colors)
    

def get_by_id(session: Session, color_id: str) -> Color:
    color: Color = session.query(Color).get(color_id)
    if color is None:
        raise UnableToFindIdError(entity_name="Color", entity_id=color_id)
    return color

def create(session: Session, color_data: ColorCreateResource) -> Color:
    new_color = Color(
        name = color_data.name,
        price = color_data.price,
        red_value = color_data.red_value,
        green_value = color_data.green_value,
        blue_value = color_data.blue_value,
    )
    session.add(new_color)
    session.commit()
    session.refresh(new_color)
    return new_color