# External Library imports
from uuid import uuid4
from typing import List
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, String, Double, ForeignKey
from pydantic import BaseModel, ConfigDict, Field

# Internal library imports
from db import Base
from app.models.brand import BrandMySQLEntity, BrandMongoEntity, BrandNeo4jEntity
from app.resources.model_resource import ModelReturnResource, ModelBaseReturnResource
from app.models.color import (
    ColorMySQLEntity,
    models_has_colors,
    ColorMongoEntity,
    ColorNeo4jEntity
)


class ModelMySQLEntity(Base):
    __tablename__ = 'models'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    brands_id: Mapped[str] = Column(String(36), ForeignKey('brands.id'), nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    image_url: Mapped[str] = Column(String(255), nullable=False)

    brand: Mapped[BrandMySQLEntity] = relationship('BrandMySQLEntity', back_populates='models', lazy=False, uselist=False)
    colors: Mapped[List[ColorMySQLEntity]] = relationship('ColorMySQLEntity', secondary=models_has_colors, back_populates='models', lazy=False)
    cars = relationship('CarMySQLEntity', back_populates='model')

    def as_resource_without_colors(self) -> ModelBaseReturnResource:
        return ModelBaseReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
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


class ModelMongoEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    brand: BrandMongoEntity
    name: str
    price: float
    image_url: str
    colors: List[ColorMongoEntity]


    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
            colors=[color.as_resource() for color in self.colors],
            name=self.name,
            price=self.price,
            image_url=self.image_url,
        )

class ModelNeo4jEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    brand: BrandNeo4jEntity
    name: str
    price: float
    image_url: str
    colors: List[ColorNeo4jEntity]


    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            brand=self.brand.as_resource(),
            colors=[color.as_resource() for color in self.colors],
            name=self.name,
            price=self.price,
            image_url=self.image_url,
        )
