# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.accessory import AccessoryReturnResource, AccessoryMySQLEntity



class AccessoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[AccessoryReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        pass

class MySQLAccessoryRepository(AccessoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[AccessoryReturnResource]:
        accessories: List[AccessoryMySQLEntity] = cast(List[AccessoryMySQLEntity], self.session.query(AccessoryMySQLEntity).all())
        return [accessory.as_resource() for accessory in accessories]

    def get_by_id(self, accessory_id: str) -> Optional[AccessoryReturnResource]:
        accessory: Optional[AccessoryMySQLEntity] = self.session.query(AccessoryMySQLEntity).get(accessory_id)
        if accessory is not None:
            return accessory.as_resource()
        return None

# Placeholder for future repositories
# class OtherDBAccessoryRepository(AccessoryRepository):
#     ...