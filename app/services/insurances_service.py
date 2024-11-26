# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.insurance_repository import InsuranceRepository, InsuranceReturnResource


def get_all(
        repository: InsuranceRepository,
        insurances_limit: Optional[int] = None
) -> List[InsuranceReturnResource]:

    if not isinstance(repository, InsuranceRepository):
        raise TypeError(f"repository must be of type InsuranceRepository, "
                        f"not {type(repository).__name__}.")
    if isinstance(insurances_limit, bool) or not (isinstance(insurances_limit, int) or insurances_limit is None):
        raise TypeError(f"insurances_limit must be of type int or None, "
                        f"not {type(insurances_limit).__name__}.")

    return repository.get_all(limit=insurances_limit)

def get_by_id(
        repository: InsuranceRepository,
        insurance_id: str
) -> InsuranceReturnResource:

    if not isinstance(repository, InsuranceRepository):
        raise TypeError(f"repository must be of type InsuranceRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(insurance_id, str):
        raise TypeError(f"insurance_id must be of type str, "
                        f"not {type(insurance_id).__name__}.")

    insurance = repository.get_by_id(insurance_id)
    if insurance is None:
        raise UnableToFindIdError(
            entity_name="Insurance",
            entity_id=insurance_id
        )
    return insurance
