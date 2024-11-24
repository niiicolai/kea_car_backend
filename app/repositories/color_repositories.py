# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database
from neo4j import Session as Neo4jSession, Query

# Internal library imports
from app.models.color import (
    ColorReturnResource,
    ColorMySQLEntity,
    ColorMongoEntity,
    ColorNeo4jEntity
)


class ColorRepository(ABC):

    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[ColorReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        pass


class MySQLColorRepository(ColorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[ColorReturnResource]:
        colors_query = self.session.query(ColorMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            colors_query = colors_query.limit(limit)
        colors: List[ColorMySQLEntity] = cast(List[ColorMySQLEntity], colors_query.all())
        return [color.as_resource() for color in colors]

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        color: Optional[ColorMySQLEntity] = self.session.get(ColorMySQLEntity, color_id)
        if color is not None:
            return color.as_resource()
        return None


class MongoDBColorRepository(ColorRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int] = None) -> List[ColorReturnResource]:
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


class Neo4jColorRepository(ColorRepository):
    def __init__(self, neo4j_session: Neo4jSession):
        self.neo4j_session = neo4j_session

    def get_all(self, limit: Optional[int] = None) -> List[ColorReturnResource]:
        query = Query("MATCH (color:Color) RETURN c")
        parameters = {}
        if limit is not None and isinstance(limit, int) and limit > 0:
            query += Query("MATCH (color:Color) RETURN color LIMIT $limit")
            parameters["limit"] = limit
        result = self.neo4j_session.run(query, parameters)
        colors = [ColorNeo4jEntity(**record["color"]).as_resource() for record in result]
        return colors

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        result = self.neo4j_session.run(
            "MATCH (color:Color {id: $id}) RETURN color",
            id=color_id
        )
        record = result.single()
        if record is not None:
            return ColorNeo4jEntity(**record["color"]).as_resource()
        return None


