# External Library imports
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

# Internal library imports
from db import Base
from app.resources.brand_resource import BrandReturnResource


class BrandMySQLEntity(Base):
    __tablename__ = 'brands'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    logo_url: Mapped[str] = Column(String(255), nullable=False)
    models = relationship('ModelMySQLEntity', back_populates='brand')


    def as_resource(self) -> BrandReturnResource:
        return BrandReturnResource(
            id=self.id,
            name=self.name,
            logo_url=self.logo_url,
        )
