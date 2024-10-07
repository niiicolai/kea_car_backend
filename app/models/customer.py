from sqlalchemy import Column, Integer, String
from db import Base
from app.resources.customer_resource import CustomerBaseResource, CustomerReturnResource


class Customer(Base):
    __tablename__ = 'customers'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    email: str = Column(String(50), unique=True, index=True, nullable=False)
    phone_number: str | None = Column(String(30), nullable=True)
    first_name: str = Column(String(45), nullable=False)
    last_name: str = Column(String(45), nullable=False)
    address: str | None = Column(String(255), nullable=True)
    
    
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
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
            address=self.address,
        )