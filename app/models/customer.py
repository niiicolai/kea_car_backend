# External Library imports
from uuid import uuid4
from typing import Optional
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship
from pydantic import BaseModel, ConfigDict, Field

# Internal library imports
from db import Base
from app.resources.customer_resource import CustomerReturnResource


class CustomerMySQLEntity(Base):
    __tablename__ = 'customers'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    email: Mapped[str] = Column(String(50), unique=True, index=True, nullable=False)
    phone_number: Mapped[Optional[str]] = Column(String(30), nullable=True)
    first_name: Mapped[str] = Column(String(45), nullable=False)
    last_name: Mapped[str] = Column(String(45), nullable=False)
    address: Mapped[Optional[str]] = Column(String(255), nullable=True)

    cars = relationship('CarMySQLEntity', back_populates='customer')

    car_purchase_view = relationship("CarPurchaseView", back_populates="car_customer", viewonly=True)



    def as_resource(self) -> CustomerReturnResource:
        return CustomerReturnResource(
            id=self.id,
            email=self.email,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )

class CustomerMongoEntity(BaseModel):  # pragma: no cover
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    email: str
    phone_number: Optional[str]
    first_name: str
    last_name: str
    address: Optional[str]

    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> CustomerReturnResource:
        return CustomerReturnResource(
            id=self.id,
            email=self.email,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )

class CustomerNeo4jEntity(BaseModel):  # pragma: no cover
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: str
    phone_number: Optional[str]
    first_name: str
    last_name: str
    address: Optional[str]

    model_config = ConfigDict(from_attributes=True)

    def as_resource(self) -> CustomerReturnResource:
        return CustomerReturnResource(
            id=self.id,
            email=self.email,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )
