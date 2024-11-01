# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.color import ColorReturnResource, ColorMySQLEntity


class ColorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[ColorReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        pass


class MySQLColorRepository(ColorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[ColorReturnResource]:
        colors: List[ColorMySQLEntity] = cast(List[ColorMySQLEntity], self.session.query(ColorMySQLEntity).all())
        return [color.as_resource() for color in colors]

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        color: Optional[ColorMySQLEntity] = self.session.query(ColorMySQLEntity).get(color_id)
        if color is not None:
            return color.as_resource()
        return None


# Placeholder for future repositories
# class OtherDBColorRepository(ColorRepository):
#     ...