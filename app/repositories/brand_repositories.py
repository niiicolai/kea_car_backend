# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.brand import BrandReturnResource, BrandMySQLEntity


class BrandRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[BrandReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        pass

class MySQLBrandRepository(BrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[BrandReturnResource]:
        brands: List[BrandMySQLEntity] = cast(List[BrandMySQLEntity], self.session.query(BrandMySQLEntity).all())
        return [brand.as_resource() for brand in brands]

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        brand: Optional[BrandMySQLEntity] = self.session.query(BrandMySQLEntity).get(brand_id)
        if brand is not None:
            return brand.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBBrandRepository(BrandRepository):
#     ...