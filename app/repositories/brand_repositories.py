# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session
from pymongo.database import Database


# Internal library imports
from app.models.brand import BrandReturnResource, BrandMySQLEntity, BrandMongoEntity


class BrandRepository(ABC):

    @abstractmethod
    def get_all(self, limit: Optional[int]) -> List[BrandReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        pass

class MySQLBrandRepository(BrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int]) -> List[BrandReturnResource]:
        brands_query = self.session.query(BrandMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            brands_query = brands_query.limit(limit)

        brands: List[BrandMySQLEntity] = cast(List[BrandMySQLEntity], brands_query.all())
        return [brand.as_resource() for brand in brands]

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        brand: Optional[BrandMySQLEntity] = self.session.query(BrandMySQLEntity).get(brand_id)
        if brand is not None:
            return brand.as_resource()
        return None


class MongoDBBrandRepository(BrandRepository):
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int]) -> List[BrandReturnResource]:
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


# Placeholder for future repositories
# class OtherDBBrandRepository(BrandRepository):
#     ...
