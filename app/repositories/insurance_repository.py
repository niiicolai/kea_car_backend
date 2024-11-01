# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.insurance import InsuranceReturnResource, InsuranceMySQLEntity


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
        insurances: List[InsuranceMySQLEntity] = cast(List[InsuranceMySQLEntity], self.session.query(InsuranceMySQLEntity).all())
        return [insurance.as_resource() for insurance in insurances]

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        insurance: Optional[InsuranceMySQLEntity] = self.session.query(InsuranceMySQLEntity).get(insurance_id)
        if insurance is not None:
            return insurance.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBInsuranceRepository(InsuranceRepository):
#     ...