from sqlalchemy import Column, Integer, String, Double
from db import Base
from app.resources.color_resource import ColorReturnResource

class Color(Base):
    __tablename__ = 'colors'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    color: str = Column(String(45), unique=True, index=True)
    price: float = Column(Double, default=0)

    def as_resource(self) -> dict:
        return ColorReturnResource(
            id=self.id,
            color=self.color,
            price=self.price
        ).to_json()