# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database

# Internal library imports
from app.models.color import ColorReturnResource, ColorMySQLEntity, ColorMongoEntity


class ColorRepository(ABC):

    @abstractmethod
    def get_all(self, limit: Optional[int]) -> List[ColorReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        pass


class MySQLColorRepository(ColorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int]) -> List[ColorReturnResource]:
        colors_query = self.session.query(ColorMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            colors_query = colors_query.limit(limit)
        colors: List[ColorMySQLEntity] = cast(List[ColorMySQLEntity], colors_query.all())
        return [color.as_resource() for color in colors]

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        color: Optional[ColorMySQLEntity] = self.session.query(ColorMySQLEntity).get(color_id)
        if color is not None:
            return color.as_resource()
        return None

class MongoDBColorRepository(ColorRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int]) -> List[ColorReturnResource]:
        colors = self.database.get_collection("colors").find(
        ).limit(0 if not limit else limit)
        colors = [
            ColorMongoEntity(
                **color
            ).as_resource()
            for color in colors]
        return colors

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        color = self.database.get_collection("colors").find_one(
            {"_id": color_id})
        if color is not None:
            return ColorMongoEntity(
                **color
            ).as_resource()
        return None

# Placeholder for future repositories
# class OtherDBColorRepository(ColorRepository):
#     ...
