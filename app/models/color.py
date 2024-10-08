from sqlalchemy import Column, Integer, String, Double
from db import Base
from app.resources.color_resource import ColorBaseResource, ColorReturnResource

class Color(Base):
    __tablename__ = 'colors'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    color_name: str = Column(String(45), unique=True, index=True, nullable=False)
    price: float = Column(Double, nullable=False)
    red_value: int = Column(Integer, nullable=False)
    green_value: int = Column(Integer, nullable=False)
    blue_value: int = Column(Integer, nullable=False)
    
    
    def validate_data(self):
        ColorBaseResource(
            color_name=self.color_name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )

    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            color_name=self.color_name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )