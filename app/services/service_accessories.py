from app.resources.accessory_resource import AccessoryReturnResource
from app.repositories.accessory_repositories import AccessoryRepository
from app.exceptions.database_errors import UnableToFindIdError
from typing import List

def get_all(repository: AccessoryRepository) -> List[AccessoryReturnResource]:
    return repository.get_all()

def get_by_id(repository: AccessoryRepository, accessory_id: str) -> AccessoryReturnResource:
    accessory = repository.get_by_id(accessory_id)
    if accessory is None:
        raise UnableToFindIdError(entity_name="Accessory", entity_id=accessory_id)
    return accessory