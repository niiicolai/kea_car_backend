from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.model_resource import ModelCreateOrUpdateResource, ModelReturnResource
from app.models.color import Color, models_has_colors
from app.models.brand import Brand

class Model(Base):
    __tablename__ = 'models'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    brands_id: Mapped[int] = Column(Integer, ForeignKey('brands.id'), nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)

    brand: Mapped[Brand] = relationship('Brand', back_populates='models', lazy=False)
    colors: Mapped[list[Color]] = relationship('Color', secondary=models_has_colors, back_populates='models', lazy=False)
    
    def validate_data(self):
        ModelCreateOrUpdateResource(
            brand_id=self.brands_id,
            color_ids=[color.id for color in self.colors],
            name=self.name,
            price=self.price,
        )

    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
            colors=[color.as_resource() for color in self.colors],
            name=self.name,
            price=self.price,
        )