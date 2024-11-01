# External Library imports
from typing import List

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.color_repositories import ColorRepository, ColorReturnResource


def get_all(repository: ColorRepository) -> List[ColorReturnResource]:
    return repository.get_all()
    

def get_by_id(repository: ColorRepository, color_id: str) -> ColorReturnResource:
    color = repository.get_by_id(color_id)
    if color is None:
        raise UnableToFindIdError(entity_name="Color", entity_id=color_id)
    return color