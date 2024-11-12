# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database

# Internal library imports
from app.resources.model_resource import BrandReturnResource
from app.models.model import (
    ModelReturnResource,
    ModelMySQLEntity,
    ModelMongoEntity,
    BrandMongoEntity,
    ColorMongoEntity
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
        model: Optional[ModelMySQLEntity] = self.session.query(ModelMySQLEntity).get(model_id)
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

        for model in models:
            brand = BrandMongoEntity(**model.get("brand"))
            colors = [ColorMongoEntity(**color) for color in model.get("colors")]
            model.update({"brand": brand, "colors": colors})

        models = [ModelMongoEntity(**model).as_resource()for model in models]
        return models

    def get_by_id(self, model_id: str) -> Optional[ModelReturnResource]:
        model = self.database.get_collection("models").find_one(
            {"_id": model_id}
        )
        if model is not None:
            return ModelMongoEntity(**model).as_resource()
        return None


# Placeholder for future repositories
# class OtherDBModelRepository(ModelRepository):
#     ...
