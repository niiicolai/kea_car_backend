from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.sales_person_resource import SalesPersonBaseResource, SalesPersonReturnResource


class SalesPerson(Base):
    __tablename__ = 'sales_people'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    email: Mapped[str] = Column(String(50), index=True, unique=True, nullable=False)
    password: Mapped[str] = Column(String(45), nullable=False)
    first_name: Mapped[str] = Column(String(45), nullable=False)
    last_name: Mapped[str] = Column(String(45), nullable=False)

    cars = relationship("Car", back_populates="sales_person", lazy=False)
    
    
    def validate_data(self):
        SalesPersonBaseResource(
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    def as_resource(self) -> SalesPersonReturnResource:
        return SalesPersonReturnResource(
            id=self.id,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )