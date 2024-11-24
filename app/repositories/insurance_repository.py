# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast

from sqlalchemy.orm import Session

# Internal library imports
from app.models.insurance import InsuranceReturnResource, InsuranceMySQLEntity


class InsuranceRepository(ABC):
    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        pass

class MySQLInsuranceRepository(InsuranceRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:
        insurances_query = self.session.query(InsuranceMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            insurances_query = insurances_query.limit(limit)
        insurances: List[InsuranceMySQLEntity] = cast(List[InsuranceMySQLEntity], insurances_query.all())
        return [insurance.as_resource() for insurance in insurances]

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        insurance: Optional[InsuranceMySQLEntity] = self.session.get(InsuranceMySQLEntity, insurance_id)
        if insurance is not None:
            return insurance.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBInsuranceRepository(InsuranceRepository):
#     ...
