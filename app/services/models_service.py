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
    filtering_by_brand: bool = brand_id is not None
    brand_resource: Optional[BrandReturnResource] = None
    if filtering_by_brand:
        brand_resource = brand_repository.get_by_id(brand_id)
        if brand_resource is None:
            raise UnableToFindIdError("Brand", brand_id)

    return model_repository.get_all(brand_resource=brand_resource, limit=brands_limit)

def get_by_id(repository: ModelRepository, model_id: str) -> ModelReturnResource:
    model_resource: Optional[ModelReturnResource] = repository.get_by_id(model_id)
    if model_resource is None:
        raise UnableToFindIdError("Model", model_id)
    return model_resource