from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.brand_resource import BrandBaseResource, BrandReturnResource


class Brand(Base):
    __tablename__ = 'brands'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    models = relationship('Model', back_populates='brand')
    
    def validate_data(self):
        BrandBaseResource(
            name=self.name,
        )

    def as_resource(self) -> BrandReturnResource:
        return BrandReturnResource(
            id=self.id,
            name=self.name,
        )