from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.insurance_resource import InsuranceBaseResource, InsuranceReturnResource

class InsuranceType(Base):
    __tablename__ = 'insurance_types'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name: Mapped[str] = Column(String(45), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    
    def validate_data(self):
        InsuranceBaseResource(
            name=self.name,
            price=self.price,
        )

    def as_resource(self) -> InsuranceReturnResource:
        return InsuranceReturnResource(
            id=self.id,
            name=self.name,
            price=self.price
        )