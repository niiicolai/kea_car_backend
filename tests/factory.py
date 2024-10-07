from db import Session
from app.models.color import Color

def create_color_in_test_db(
    session: Session,
    color_name: str = "black",
    price: float = 78.99
    ) -> Color:
    new_color = Color(
        color_name = color_name,
        price = price
    )
    new_color.validate_data()
    session.add(new_color)
    session.commit()
    session.refresh(new_color)
    return new_color

