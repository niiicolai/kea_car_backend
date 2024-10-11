from sqlalchemy import Table, Column, ForeignKey, Integer, String, Double
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.insurance_resource import InsuranceBaseResource, InsuranceReturnResource

cars_has_insurances = Table(
    'cars_has_insurances',
    Base.metadata,
    Column('cars_id', Integer, ForeignKey('cars.id'), primary_key=True),
    Column('insurances_id', Integer, ForeignKey('insurances.id'), primary_key=True),
)

class Insurance(Base):
    __tablename__ = 'insurances'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name: Mapped[str] = Column(String(45), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)

    cars = relationship('Car', secondary=cars_has_insurances, back_populates='insurances', lazy=False)
    
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