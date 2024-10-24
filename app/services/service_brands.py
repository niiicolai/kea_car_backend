from app.resources.brand_resource import BrandReturnResource
from app.repositories.brand_repositories import BrandRepository
from typing import List

def get_all(repository: BrandRepository) -> List[BrandReturnResource]:
    return repository.get_all()