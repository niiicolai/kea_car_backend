from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.model_resource import ModelBaseResource, ModelReturnResource
from app.models.brand import Brand

class Model(Base):
    __tablename__ = 'models'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    brands_id: Mapped[int] = Column(Integer, ForeignKey('brands.id'), nullable=False)
    model_name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    brand: Mapped[Brand] = relationship('Brand', back_populates='models', lazy=False)
    
    def validate_data(self):
        ModelBaseResource(
            carmodel_name=self.model_name,
            price=self.price,
        )

    def as_resource(self) -> ModelReturnResource:
        return ModelReturnResource(
            id=self.id,
            carmodel_name=self.model_name,
            price=self.price,
            brand=self.brand.as_resource(),
        )