from sqlalchemy import Column, Integer, String, Double
from db import Base
from app.resources.color_resource import ColorBaseResource, ColorReturnResource

class Color(Base):
    __tablename__ = 'colors'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    color_name: str = Column(String(45), unique=True, index=True, nullable=False)
    price: float = Column(Double, default=0, nullable=False)
    
    def validate_data(self):
        ColorBaseResource(
            color_name=self.color_name,
            price=self.price,
        )

    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            color_name=self.color_name,
            price=self.price
        )