from abc import ABC, abstractmethod
from typing import List, cast
from app.resources.accessory_resource import AccessoryReturnResource
from app.models.accessory import Accessory
from sqlalchemy.orm import Session


class AccessoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[AccessoryReturnResource]:
        pass

class MySQLAccessoryRepository(AccessoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[AccessoryReturnResource]:
        accessories: List[Accessory] = cast(List[Accessory], self.session.query(Accessory).all())
        return [accessory.as_resource() for accessory in accessories]


# Placeholder for future repositories
# class OtherDBAccessoryRepository(AccessoryRepository):
#     ...