# External Library imports
from typing import List, Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.color_repositories import ColorRepository, ColorReturnResource


def get_all(repository: ColorRepository, colors_limit: Optional[int] = None) -> List[ColorReturnResource]:
    if not isinstance(repository, ColorRepository):
        raise TypeError(f"repository must be of type ColorRepository, not {type(repository)}")
    if not (isinstance(colors_limit, int) or colors_limit is None):
        raise TypeError(f"colors_limit must be of type int or None, not {type(colors_limit)}")

    return repository.get_all(limit=colors_limit)
    

def get_by_id(repository: ColorRepository, color_id: str) -> ColorReturnResource:
    if not isinstance(repository, ColorRepository):
        raise TypeError(f"repository must be of type ColorRepository, not {type(repository)}")
    if not isinstance(color_id, str):
        raise TypeError(f"color_id must be of type str, not {type(color_id)}")

    color = repository.get_by_id(color_id)
    if color is None:
        raise UnableToFindIdError(entity_name="Color", entity_id=color_id)
    return color