# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.brand_repositories import BrandRepository, BrandReturnResource


def get_all(
        repository: BrandRepository,
        brands_limit: Optional[int] = None
) -> List[BrandReturnResource]:

    if not isinstance(repository, BrandRepository):
        raise TypeError(f"repository must be of type BrandRepository, "
                        f"not {type(repository).__name__}.")
    if not (isinstance(brands_limit, int) or brands_limit is None):
        raise TypeError(f"brands_limit must be of type int or None, "
                        f"not {type(brands_limit).__name__}.")

    return repository.get_all(limit=brands_limit)

def get_by_id(
        repository: BrandRepository,
        brand_id: str
) -> BrandReturnResource:

    if not isinstance(repository, BrandRepository):
        raise TypeError(f"repository must be of type BrandRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(brand_id, str):
        raise TypeError(f"brand_id must be of type str, "
                        f"not {type(brand_id).__name__}.")

    brand = repository.get_by_id(brand_id)
    if brand is None:
        raise UnableToFindIdError(
            entity_name="Accessory",
            entity_id=brand_id
        )
    return brand
