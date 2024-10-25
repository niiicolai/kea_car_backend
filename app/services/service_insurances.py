from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.insurance_repository import InsuranceRepository, InsuranceReturnResource
from typing import List

def get_all(repository: InsuranceRepository) -> List[InsuranceReturnResource]:
    return repository.get_all()

def get_by_id(repository: InsuranceRepository, insurance_id: str) -> InsuranceReturnResource:
    insurance = repository.get_by_id(insurance_id)
    if insurance is None:
        raise UnableToFindIdError(entity_name="Insurance", entity_id=insurance_id)
    return insurance