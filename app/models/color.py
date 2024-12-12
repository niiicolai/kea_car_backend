# External Library imports
from uuid import uuid4
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Table, Column, Integer, String, Double, ForeignKey
from pydantic import BaseModel, ConfigDict, Field

# Internal library imports
from db import Base
from app.resources.color_resource import ColorReturnResource


models_has_colors = Table(
    'models_has_colors',
    Base.metadata,
    Column('models_id', String(36), ForeignKey('models.id'), primary_key=True, nullable=False),
    Column('colors_id', String(36), ForeignKey('colors.id'), primary_key=True, nullable=False),
)

class ColorMySQLEntity(Base):
    __tablename__ = 'colors'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    name: Mapped[str] = Column(String(45), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    red_value: Mapped[int] = Column(Integer, nullable=False)
    green_value: Mapped[int] = Column(Integer, nullable=False)
    blue_value: Mapped[int] = Column(Integer, nullable=False)
    models = relationship('ModelMySQLEntity', secondary=models_has_colors, back_populates='colors')
    cars = relationship('CarMySQLEntity', back_populates='color')


    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            name=self.name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )

class ColorMongoEntity(BaseModel):  # pragma: no cover
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    name: str
    price: float
    red_value: int
    green_value: int
    blue_value: int

    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            name=self.name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )


class ColorNeo4jEntity(BaseModel):  # pragma: no cover
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    price: float
    red_value: int
    green_value: int
    blue_value: int

    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> ColorReturnResource:
        return ColorReturnResource(
            id=self.id,
            name=self.name,
            price=self.price,
            red_value=self.red_value,
            green_value=self.green_value,
            blue_value=self.blue_value,
        )
