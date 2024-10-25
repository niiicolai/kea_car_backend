# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.purchase import Purchase
from app.resources.purchase_resource import PurchaseReturnResource, PurchaseCreateResource, CarReturnResource




class PurchaseRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[PurchaseReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        pass

    @abstractmethod
    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        pass

    @abstractmethod
    def create(self, car_resource: CarReturnResource) -> PurchaseReturnResource:
        pass

    @abstractmethod
    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        pass


class MySQLPurchaseRepository(PurchaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[PurchaseReturnResource]:
        purchases: List[Purchase] = cast(List[Purchase], self.session.query(Purchase).all())
        return [purchase.as_resource() for purchase in purchases]

    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        purchase: Optional[Purchase] = self.session.query(Purchase).get(purchase_id)
        if purchase is not None:
            return purchase.as_resource()
        return None

    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        purchase: Optional[Purchase] = self.session.query(Purchase).filter_by(cars_id=car_resource.id).first()
        if purchase is not None:
            return purchase.as_resource()
        return None

    def create(self, car_resource: CarReturnResource) -> PurchaseReturnResource:
        new_purchase = Purchase(
            cars_id=car_resource.id,
        )
        self.session.add(new_purchase)
        self.session.commit()
        self.session.refresh(new_purchase)

        return new_purchase.as_resource()

    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        return self.session.query(Purchase).filter_by(cars_id=car_resource.id).first() is not None

# Placeholder for future repositories
# class OtherDBPurchaseRepository(PurchaseRepository):
#     ...