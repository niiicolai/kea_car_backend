from abc import ABC, abstractmethod
from typing import List, Optional, cast
from app.resources.brand_resource import BrandReturnResource
from app.models.brand import Brand
from sqlalchemy.orm import Session


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
        brands: List[Brand] = cast(List[Brand], self.session.query(Brand).all())
        return [brand.as_resource() for brand in brands]

    def get_by_id(self, brand_id: str) -> Optional[BrandReturnResource]:
        brand: Optional[Brand] = self.session.query(Brand).get(brand_id)
        if brand is not None:
            return brand.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBBrandRepository(BrandRepository):
#     ...