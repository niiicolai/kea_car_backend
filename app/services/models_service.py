# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.model_repositories import ModelRepository, ModelReturnResource
from app.repositories.brand_repositories import BrandRepository, BrandReturnResource


def get_all(
        model_repository: ModelRepository,
        brand_repository: BrandRepository,
        brand_id: Optional[str] = None,
        brands_limit: Optional[int] = None) -> List[ModelReturnResource]:
    if not isinstance(model_repository, ModelRepository):
        raise TypeError(f"model_repository must be of type ModelRepository, not {type(model_repository).__name__}.")
    if not isinstance(brand_repository, BrandRepository):
        raise TypeError(f"brand_repository must be of type BrandRepository, not {type(brand_repository).__name__}.")
    if not isinstance(brand_id, str):
        raise TypeError(f"brand_id must be of type str, not {type(brand_id)}")
    if not (isinstance(brands_limit, int) or brands_limit is None):
        raise TypeError(f"brands_limit must be of type int or None, not {type(brands_limit).__name__}.")

    filtering_by_brand: bool = brand_id is not None
    brand_resource: Optional[BrandReturnResource] = None
    if filtering_by_brand:
        brand_resource = brand_repository.get_by_id(brand_id)
        if brand_resource is None:
            raise UnableToFindIdError("Brand", brand_id)

    return model_repository.get_all(brand_resource=brand_resource, limit=brands_limit)

def get_by_id(repository: ModelRepository, model_id: str) -> ModelReturnResource:
    if not isinstance(repository, ModelRepository):
        raise TypeError(f"repository must be of type ModelRepository, not {type(repository).__name__}.")
    if not isinstance(model_id, str):
        raise TypeError(f"model_id must be of type str, not {type(model_id).__name__}.")

    model_resource: Optional[ModelReturnResource] = repository.get_by_id(model_id)
    if model_resource is None:
        raise UnableToFindIdError("Model", model_id)
    return model_resource