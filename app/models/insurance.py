from sqlalchemy import Column, Integer, String, Double
from db import Base
from app.resources.insurance_resource import InsuranceBaseResource, InsuranceReturnResource

class InsuranceType(Base):
    __tablename__ = 'insurance_types'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    insurance_name: str = Column(String(45), unique=True, index=True, nullable=False)
    price: float = Column(Double, nullable=False)
    
    def validate_data(self):
        InsuranceBaseResource(
            insurance_name=self.insurance_name,
            price=self.price,
        )

    def as_resource(self) -> InsuranceReturnResource:
        return InsuranceReturnResource(
            id=self.id,
            insurance_name=self.insurance_name,
            price=self.price
        )