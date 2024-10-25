# External Library imports
from uuid import uuid4
from typing import Optional
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

# Internal library imports
from db import Base
from app.resources.customer_resource import CustomerBaseResource, CustomerReturnResource


class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    email: Mapped[str] = Column(String(50), unique=True, index=True, nullable=False)
    phone_number: Mapped[Optional[str]] = Column(String(30), nullable=True)
    first_name: Mapped[str] = Column(String(45), nullable=False)
    last_name: Mapped[str] = Column(String(45), nullable=False)
    address: Mapped[Optional[str]] = Column(String(255), nullable=True)

    cars = relationship('Car', back_populates='customer')
    
    
    def validate_data(self):
        CustomerBaseResource(
            email=self.email,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )

    def as_resource(self) -> CustomerReturnResource:
        return CustomerReturnResource(
            id=self.id,
            email=self.email,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )