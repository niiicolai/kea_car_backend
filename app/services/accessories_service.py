# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.accessory_repositories import AccessoryRepository, AccessoryReturnResource


def get_all(repository: AccessoryRepository, accessory_limit: Optional[int] = None) -> List[AccessoryReturnResource]:
    if not isinstance(repository, AccessoryRepository):
        raise TypeError(f"repository must be of type AccessoryRepository, not {type(repository)}")
    if not (isinstance(accessory_limit, int) or accessory_limit is None):
        raise TypeError(f"accessory_limit must be of type int or None, not {type(accessory_limit)}")

    return repository.get_all(limit=accessory_limit)

def get_by_id(repository: AccessoryRepository, accessory_id: str) -> AccessoryReturnResource:
    if not isinstance(repository, AccessoryRepository):
        raise TypeError(f"repository must be of type AccessoryRepository, not {type(repository)}")
    if not isinstance(accessory_id, str):
        raise TypeError(f"accessory_id must be of type str, not {type(accessory_id)}")

    accessory = repository.get_by_id(accessory_id)
    if accessory is None:
        raise UnableToFindIdError(entity_name="Accessory", entity_id=accessory_id)
    return accessory