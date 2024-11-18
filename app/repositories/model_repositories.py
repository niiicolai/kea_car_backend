# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database
from neo4j import Session as Neo4jSession

# Internal library imports
from app.resources.model_resource import BrandReturnResource
from app.models.model import (
    ModelReturnResource,
    ModelMySQLEntity,
    ModelMongoEntity,
    BrandMongoEntity,
    ColorMongoEntity,
    ModelNeo4jEntity,
    BrandNeo4jEntity,
    ColorNeo4jEntity
)


class ModelRepository(ABC):
    @abstractmethod
    def get_all(self, brand_resource: Optional[BrandReturnResource], limit: Optional[int]) -> List[ModelReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, model_id: str) -> Optional[ModelReturnResource]:
        pass

class MySQLModelRepository(ModelRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, brand_resource: Optional[BrandReturnResource], limit: Optional[int]) -> List[ModelReturnResource]:
        models_query = self.session.query(ModelMySQLEntity)
        if brand_resource is not None and isinstance(brand_resource, BrandReturnResource):
            models_query = models_query.filter_by(brands_id=brand_resource.id)

        if limit is not None and isinstance(limit, int) and limit > 0:
            models_query = models_query.limit(limit)

        models: List[ModelMySQLEntity] = cast(List[ModelMySQLEntity], models_query.all())
        return [model.as_resource() for model in models]


    def get_by_id(self, model_id: str) -> Optional[ModelReturnResource]:
        model: Optional[ModelMySQLEntity] = self.session.get(ModelMySQLEntity, model_id)
        if model is not None:
            return model.as_resource()
        return None

class MongoDBModelRepository(ModelRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, brand_resource: Optional[BrandReturnResource], limit: Optional[int]) -> List[ModelReturnResource]:
        models = self.database.get_collection("models")
        if brand_resource is not None and isinstance(brand_resource, BrandReturnResource):
            models = models.find(
                {"brand._id": brand_resource.id}
            )
        else:
            models = models.find()
        models = models.limit(0 if not limit else limit)
        retrieved_models: List[ModelReturnResource] = []
        for model in models:
            brand = BrandMongoEntity(**model.get("brand"))
            colors = [ColorMongoEntity(**color) for color in model.get("colors")]
            model.update({"brand": brand, "colors": colors})
            retrieved_model = ModelMongoEntity(**model).as_resource()
            retrieved_models.append(retrieved_model)

        return retrieved_models

    def get_by_id(self, model_id: str) -> Optional[ModelReturnResource]:
        model = self.database.get_collection("models").find_one(
            {"_id": model_id}
        )
        if model is not None:
            return ModelMongoEntity(**model).as_resource()
        return None

class Neo4jModelRepository(ModelRepository):
    def __init__(self, neo4j_session: Neo4jSession):
        self.neo4j_session = neo4j_session

    def get_all(self, brand_resource: Optional[BrandReturnResource], limit: Optional[int]) -> List[ModelReturnResource]:
        query = """
        MATCH (m:Model)-[:BELONGS_TO]->(b:Brand)
        OPTIONAL MATCH (m)-[:HAS_COLOR]->(c:Color)
        RETURN m, b, collect(c) as colors
        """
        parameters = {}
        if brand_resource is not None and isinstance(brand_resource, BrandReturnResource):
            query = """
            MATCH (m:Model)-[:BELONGS_TO]->(b:Brand {id: $brand_id})
            OPTIONAL MATCH (m)-[:HAS_COLOR]->(c:Color)
            RETURN m, b, collect(c) as colors
            """
            parameters["brand_id"] = brand_resource.id
        if limit is not None and isinstance(limit, int) and limit > 0:
            query += " LIMIT $limit"
            parameters["limit"] = limit
        result = self.neo4j_session.run(query, parameters)
        models: List[ModelReturnResource] = []
        for record in result:
            brand = BrandNeo4jEntity(**record["b"])
            colors = [ColorNeo4jEntity(**color) for color in record["colors"]]
            model = ModelNeo4jEntity(**record["m"], brand=brand, colors=colors)
            models.append(model.as_resource())
        return models

    def get_by_id(self, model_id: str) -> Optional[ModelReturnResource]:
        query = """
        MATCH (m:Model {id: $model_id})-[:BELONGS_TO]->(b:Brand)
        OPTIONAL MATCH (m)-[:HAS_COLOR]->(c:Color)
        RETURN m, b, collect(c) as colors
        """
        result = self.neo4j_session.run(query, model_id=model_id)
        record = result.single()
        if record:
            brand = BrandNeo4jEntity(**record["b"])
            colors = [ColorNeo4jEntity(**color) for color in record["colors"]]
            model = ModelNeo4jEntity(**record["m"], brand=brand, colors=colors)
            return model.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBModelRepository(ModelRepository):
#     ...
