from abc import ABC, abstractmethod
from typing import Optional, List, cast
from app.resources.insurance_resource import InsuranceReturnResource
from app.models.insurance import Insurance
from sqlalchemy.orm import Session


class InsuranceRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[InsuranceReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        pass

class MySQLInsuranceRepository(InsuranceRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[InsuranceReturnResource]:
        insurances: List[Insurance] = cast(List[Insurance], self.session.query(Insurance).all())
        return [insurance.as_resource() for insurance in insurances]

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        insurance: Optional[Insurance] = self.session.query(Insurance).get(insurance_id)
        if insurance is not None:
            return insurance.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBInsuranceRepository(InsuranceRepository):
#     ...