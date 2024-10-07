from sqlalchemy import Column, Integer, String
from db import Base
from app.resources.brand_resource import BrandBaseResource, BrandReturnResource


class Brand(Base):
    __tablename__ = 'brands'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    brand_name: str = Column(String(60), unique=True, index=True, nullable=False)
    
    def validate_data(self):
        BrandBaseResource(
            brand_name=self.brand_name,
        )

    def as_resource(self) -> BrandReturnResource:
        return BrandReturnResource(
            id=self.id,
            brand_name=self.brand_name,
        )