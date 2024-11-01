# External Library imports
from uuid import uuid4
from typing import Optional, List
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, String, Double, ForeignKey

# Internal library imports
from db import Base
from app.models.brand import BrandMySQLEntity
from app.resources.model_resource import ModelReturnResource
from app.models.color import ColorMySQLEntity, models_has_colors


class ModelMySQLEntity(Base):
    __tablename__ = 'models'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    brands_id: Mapped[str] = Column(String(36), ForeignKey('brands.id'), nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    image_url: Mapped[Optional[str]] = Column(String(255), nullable=False)

    brand: Mapped[BrandMySQLEntity] = relationship('BrandMySQLEntity', back_populates='models', lazy=False)
    colors: Mapped[List[ColorMySQLEntity]] = relationship('ColorMySQLEntity', secondary=models_has_colors, back_populates='models', lazy=False)
    cars = relationship('CarMySQLEntity', back_populates='model')


    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
            colors=[color.as_resource() for color in self.colors],
            name=self.name,
            price=self.price,
            image_url=self.image_url,
        )