from app.resources.accessory_resource import AccessoryReturnResource
from app.repositories.accessory_repositories import AccessoryRepository
from typing import List

def get_all(repository: AccessoryRepository) -> List[AccessoryReturnResource]:
    return repository.get_all()