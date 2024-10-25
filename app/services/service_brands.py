# External Library imports
from typing import List

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.brand_repositories import BrandRepository, BrandReturnResource


def get_all(repository: BrandRepository) -> List[BrandReturnResource]:
    return repository.get_all()

def get_by_id(repository: BrandRepository, brand_id: str) -> BrandReturnResource:
    brand = repository.get_by_id(brand_id)
    if brand is None:
        raise UnableToFindIdError(entity_name="Accessory", entity_id=brand_id)
    return brand