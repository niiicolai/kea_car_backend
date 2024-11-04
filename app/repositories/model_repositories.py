# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.resources.model_resource import BrandReturnResource
from app.models.model import ModelReturnResource, ModelMySQLEntity


class ModelRepository(ABC):
    @abstractmethod
    def get_all(self, brand_resource: Optional[BrandReturnResource], limit: Optional[int]) -> List[ModelReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, insurance_id: str) -> Optional[ModelReturnResource]:
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

# Placeholder for future repositories
# class OtherDBModelRepository(ModelRepository):
#     ...