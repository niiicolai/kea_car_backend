from sqlalchemy import Column, Integer, String
from db import Base
from app.resources.sales_person_resource import SalesPersonValidationResource, SalesPersonReturnResource
import random
import string

def generate_random_six_letters():
    letters = string.ascii_letters  # Only uppercase and lowercase letters
    return ''.join(random.choice(letters) for _ in range(6))

class SalesPerson(Base):
    __tablename__ = 'sales_people'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    employee_number: str = Column(String(6), unique=True, index=True, nullable=False, insert_default=generate_random_six_letters)
    first_name: str = Column(String(45), nullable=False)
    last_name: str = Column(String(45), nullable=False)
    
    
    def validate_data(self):
        SalesPersonValidationResource(
            first_name=self.first_name,
            last_name=self.last_name,
            employee_number=self.employee_number,
        )

    def as_resource(self) -> SalesPersonReturnResource:
        return SalesPersonReturnResource(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            employee_number=self.employee_number,
        )