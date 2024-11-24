# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session as MySQLSession
from pymongo.database import Database
from neo4j import Session as Neo4jSession

# Internal library imports
from app.models.accessory import (
    AccessoryReturnResource,
    AccessoryMySQLEntity,
    AccessoryMongoEntity,
    AccessoryNeo4jEntity
)



class AccessoryRepository(ABC):
    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[AccessoryReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        pass

class MySQLAccessoryRepository(AccessoryRepository):
    def __init__(self, session: MySQLSession):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[AccessoryReturnResource]:
        accessories_query = self.session.query(AccessoryMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            accessories_query = accessories_query.limit(limit)
        accessories: List[AccessoryMySQLEntity] = cast(List[AccessoryMySQLEntity], accessories_query.all())
        return [accessory.as_resource() for accessory in accessories]

    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        accessory: Optional[AccessoryMySQLEntity] = self.session.get(AccessoryMySQLEntity, accessory_id)
        if accessory is not None:
            return accessory.as_resource()
        return None


class MongoDBAccessoryRepository(AccessoryRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int] = None) -> List[AccessoryReturnResource]:
        accessories = self.database.get_collection("accessories").find(
        ).limit(0 if not limit else limit)
        accessories = [
            AccessoryMongoEntity(
                **accessory
            ).as_resource()
            for accessory in accessories]
        return accessories

    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        accessory = self.database.get_collection("accessories").find_one(
            {"_id": accessory_id})
        if accessory is not None:
            return AccessoryMongoEntity(
                **accessory
            ).as_resource()
        return None

class Neo4jAccessoryRepository(AccessoryRepository):
    def __init__(self, neo4j_session: Neo4jSession):
        self.neo4j_session = neo4j_session

    def get_all(self, limit: Optional[int] = None) -> List[AccessoryReturnResource]:
        query = "MATCH (a:Accessory) RETURN a"
        parameters = {}
        if limit is not None and isinstance(limit, int) and limit > 0:
            query += " LIMIT $limit"
            parameters["limit"] = limit
        result = self.neo4j_session.run(query, parameters)
        accessories = [AccessoryNeo4jEntity(**record["a"]).as_resource() for record in result]
        return accessories

    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        result = self.neo4j_session.run(
            "MATCH (a:Accessory {id: $id}) RETURN a",
            id=accessory_id
        )
        record = result.single()
        if record:
            return AccessoryNeo4jEntity(**record["a"]).as_resource()
        return None

# Placeholder for future repositories
# class OtherDBAccessoryRepository(AccessoryRepository):
#     ...
