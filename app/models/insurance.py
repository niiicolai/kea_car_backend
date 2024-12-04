# External Library imports
from uuid import uuid4
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Table, Column, ForeignKey, String, Double
from pydantic import BaseModel, ConfigDict, Field

# Internal library imports
from db import Base
from app.resources.insurance_resource import InsuranceReturnResource


cars_has_insurances = Table(
    'cars_has_insurances',
    Base.metadata,
    Column('cars_id', String(36), ForeignKey('cars.id'), primary_key=True, nullable=False),
    Column('insurances_id', String(36), ForeignKey('insurances.id'), primary_key=True, nullable=False),
)

class InsuranceMySQLEntity(Base):
    __tablename__ = 'insurances'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    name: Mapped[str] = Column(String(45), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)

    cars = relationship('CarMySQLEntity', secondary=cars_has_insurances, back_populates='insurances')


    def as_resource(self) -> InsuranceReturnResource:
        return InsuranceReturnResource(
            id=self.id,
            name=self.name,
            price=self.price
        )

class InsuranceMongoEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    name: str
    price: float
    
    model_config = ConfigDict(from_attributes=True)


    def as_resource(self) -> InsuranceReturnResource:
        return InsuranceReturnResource(
            id=self.id,
            name=self.name,
            price=self.price
        )


class InsuranceNeo4jEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    price: float
    
    model_config = ConfigDict(from_attributes=True)


    def as_resource(self) -> InsuranceReturnResource:
        return InsuranceReturnResource(
            id=self.id,
            name=self.name,
            price=self.price
        ) 