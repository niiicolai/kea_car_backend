from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from typing import Optional
from db import Base
from app.resources.customer_resource import CustomerBaseResource, CustomerReturnResource


class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    email: Mapped[str] = Column(String(50), unique=True, index=True, nullable=False)
    phone_number: Mapped[Optional[str]] = Column(String(30), nullable=True)
    first_name: Mapped[str] = Column(String(45), nullable=False)
    last_name: Mapped[str] = Column(String(45), nullable=False)
    address: Mapped[Optional[str]] = Column(String(255), nullable=True)
    
    
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