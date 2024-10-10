from sqlalchemy import Table, Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.color_resource import ColorBaseResource, ColorReturnResource

models_has_colors = Table(
    'models_has_colors',
    Base.metadata,
    Column('models_id', Integer, ForeignKey('models.id'), primary_key=True),
    Column('colors_id', Integer, ForeignKey('colors.id'), primary_key=True),
)

class Color(Base):
    __tablename__ = 'colors'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name: Mapped[str] = Column(String(45), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    red_value: Mapped[int] = Column(Integer, nullable=False)
    green_value: Mapped[int] = Column(Integer, nullable=False)
    blue_value: Mapped[int] = Column(Integer, nullable=False)
    models = relationship('Model', secondary=models_has_colors, back_populates='colors', lazy=False)
    cars = relationship('Car', back_populates='color', lazy=False)
    
    
    def validate_data(self):
        ColorBaseResource(
            name=self.name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )

    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            name=self.name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )