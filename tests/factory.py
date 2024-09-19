from db import Session
from app.models.color import Color

def create_color_in_test_db(
    session: Session,
    color: str = "Black",
    price: float = 78.99
    ) -> Color:
    new_color = Color(
        color = color,
        price = price
    )
    session.add(new_color)
    session.commit()
    session.refresh(new_color)
    return new_color
    