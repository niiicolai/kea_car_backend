# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database
from neo4j import Session as Neo4jSession, Query

# Internal library imports
from app.models.brand import (
    BrandReturnResource,
    BrandMySQLEntity,
    BrandMongoEntity,
    BrandNeo4jEntity
)


class BrandRepository(ABC):  # pragma: no cover

    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[BrandReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        pass


class MySQLBrandRepository(BrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[BrandReturnResource]:
        brands_query = self.session.query(BrandMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            brands_query = brands_query.limit(limit)

        brands: List[BrandMySQLEntity] = cast(List[BrandMySQLEntity], brands_query.all())
        return [brand.as_resource() for brand in brands]

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        brand: Optional[BrandMySQLEntity] = self.session.get(BrandMySQLEntity, brand_id)
        if brand is not None:
            return brand.as_resource()
        return None


class MongoDBBrandRepository(BrandRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int] = None) -> List[BrandReturnResource]:
        brands = self.database.get_collection("brands").find(
        ).limit(0 if not limit else limit)
        brands = [
            BrandMongoEntity(
                **brand
            ).as_resource()
            for brand in brands]
        return brands

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        brand = self.database.get_collection("brands").find_one(
            {"_id": brand_id})
        if brand is not None:
            return BrandMongoEntity(
                **brand
            ).as_resource()
        return None


class Neo4jBrandRepository(BrandRepository):  # pragma: no cover
    def __init__(self, neo4j_session: Neo4jSession):
        self.neo4j_session = neo4j_session

    def get_all(self, limit: Optional[int] = None) -> List[BrandReturnResource]:
        query = Query("MATCH (b:Brand) RETURN b")
        parameters = {}
        if limit is not None and isinstance(limit, int) and limit > 0:
            query += Query("MATCH (b:Brand) RETURN b LIMIT $limit")
            parameters["limit"] = limit
        result = self.neo4j_session.run(query, parameters)
        brands = [BrandNeo4jEntity(**record["b"]).as_resource() for record in result]
        return brands

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        result = self.neo4j_session.run(
            "MATCH (b:Brand {id: $id}) RETURN b",
            id=brand_id
        )
        record = result.single()
        if record is not None:
            return BrandNeo4jEntity(**record["b"]).as_resource()
        return None
