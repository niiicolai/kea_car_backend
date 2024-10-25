from app.repositories.color_repositories import ColorRepository, ColorReturnResource, ColorCreateResource
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from typing import List

def get_all(repository: ColorRepository) -> List[ColorReturnResource]:
    return repository.get_all()
    

def get_by_id(repository: ColorRepository, color_id: str) -> ColorReturnResource:
    color = repository.get_by_id(color_id)
    if color is None:
        raise UnableToFindIdError(entity_name="Color", entity_id=color_id)
    return color

def create(repository: ColorRepository, color_create_data: ColorCreateResource) -> ColorReturnResource:
    if repository.is_name_taken(color_create_data.name):
        raise AlreadyTakenFieldValueError(entity_name="Color", field="name", value=color_create_data.name)
    return repository.create(color_create_data)