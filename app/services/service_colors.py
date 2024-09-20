from app.models.color import Color
from app.resources.color_resource import ColorCreateResource
from app.models.color import Color
from sqlalchemy.orm import Session

def get_all(session: Session) -> list[dict]:
    colors = session.query(Color).all()
    return [color.as_resource() for color in colors]

def get_by_id(session: Session, color_id: int) -> dict:
    color: Color = session.query(Color).get(color_id)
    if color is None:
        raise ValueError(f"color with id {color_id} does not exist.")
    return color.as_resource()

def create(session: Session, color_data: ColorCreateResource) -> dict:
    new_color = Color(
        color = color_data.color,
        price = color_data.price
    )
    session.add(new_color)
    session.commit()
    session.refresh(new_color)
    return new_color.as_resource()