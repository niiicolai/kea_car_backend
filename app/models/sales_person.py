# External Library imports
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

# Internal library imports
from db import Base
from app.resources.sales_person_resource import SalesPersonReturnResource



class SalesPersonMySQLEntity(Base):
    __tablename__ = 'sales_people'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    email: Mapped[str] = Column(String(100), index=True, unique=True, nullable=False)
    hashed_password: Mapped[str] = Column(String(130), nullable=False)
    first_name: Mapped[str] = Column(String(45), nullable=False)
    last_name: Mapped[str] = Column(String(45), nullable=False)

    cars = relationship("CarMySQLEntity", back_populates="sales_person")


    def as_resource(self) -> SalesPersonReturnResource:
        return SalesPersonReturnResource(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
        )