from sqlalchemy import Column, String, Double, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.model_resource import ModelCreateOrUpdateResource, ModelReturnResource
from app.models.color import Color, models_has_colors
from app.models.brand import Brand
from uuid import uuid4
from typing import Optional, List

class Model(Base):
    __tablename__ = 'models'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    brands_id: Mapped[str] = Column(String(36), ForeignKey('brands.id'), nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    image_url: Mapped[Optional[str]] = Column(String(255), nullable=True)

    brand: Mapped[Brand] = relationship('Brand', back_populates='models', lazy=False)
    colors: Mapped[List[Color]] = relationship('Color', secondary=models_has_colors, back_populates='models', lazy=False)
    cars = relationship('Car', back_populates='model')
    
    def validate_data(self):
        ModelCreateOrUpdateResource(
            brand_id=self.brands_id,
            color_ids=[color.id for color in self.colors],
            name=self.name,
            price=self.price,
            image_url=self.image_url,
        )

    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
            colors=[color.as_resource() for color in self.colors],
            name=self.name,
            price=self.price,
            image_url=self.image_url,
        )