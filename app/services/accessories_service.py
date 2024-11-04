# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.accessory_repositories import AccessoryRepository, AccessoryReturnResource


def get_all(repository: AccessoryRepository, accessory_limit: Optional[int] = None) -> List[AccessoryReturnResource]:
    return repository.get_all(limit=accessory_limit)

def get_by_id(repository: AccessoryRepository, accessory_id: str) -> AccessoryReturnResource:
    accessory = repository.get_by_id(accessory_id)
    if accessory is None:
        raise UnableToFindIdError(entity_name="Accessory", entity_id=accessory_id)
    return accessory