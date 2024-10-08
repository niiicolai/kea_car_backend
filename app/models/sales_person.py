from sqlalchemy import Column, Integer, String
from db import Base
from app.resources.sales_person_resource import SalesPersonBaseResource, SalesPersonReturnResource


class SalesPerson(Base):
    __tablename__ = 'sales_people'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    username: str = Column(String(45), index=True, unique=True, nullable=False)
    password: str = Column(String(45), nullable=False)
    first_name: str = Column(String(45), nullable=False)
    last_name: str = Column(String(45), nullable=False)
    
    
    def validate_data(self):
        SalesPersonBaseResource(
            username=self.username,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    def as_resource(self) -> SalesPersonReturnResource:
        return SalesPersonReturnResource(
            id=self.id,
            username=self.username,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
        )