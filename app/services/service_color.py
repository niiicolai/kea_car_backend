from app.models.color import Color
#from app.resources.color_resource import 
from sqlalchemy.orm import Session

def get_all(session: Session) -> list[dict]:
    colors = session.query(Color).all()
    return [color.as_resource() for color in colors]