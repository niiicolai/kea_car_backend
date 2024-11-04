# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.purchase import PurchaseReturnResource, PurchaseMySQLEntity
from app.resources.purchase_resource import PurchaseCreateResource, CarReturnResource




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
    def create(self, purchase_create_data: PurchaseCreateResource, car_resource: CarReturnResource) -> PurchaseReturnResource:
        pass

    @abstractmethod
    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        pass


class MySQLPurchaseRepository(PurchaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[PurchaseReturnResource]:
        purchases: List[PurchaseMySQLEntity] = cast(List[PurchaseMySQLEntity], self.session.query(PurchaseMySQLEntity).all())
        return [purchase.as_resource() for purchase in purchases]

    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        purchase: Optional[PurchaseMySQLEntity] = self.session.query(PurchaseMySQLEntity).get(purchase_id)
        if purchase is not None:
            return purchase.as_resource()
        return None

    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        purchase: Optional[PurchaseMySQLEntity] = self.session.query(PurchaseMySQLEntity).filter_by(cars_id=car_resource.id).first()
        if purchase is not None:
            return purchase.as_resource()
        return None

    def create(self, purchase_create_data: PurchaseCreateResource, car_resource: CarReturnResource) -> PurchaseReturnResource:
        new_purchase = PurchaseMySQLEntity(
            cars_id=car_resource.id,
            date_of_purchase=purchase_create_data.date_of_purchase
        )
        self.session.add(new_purchase)
        self.session.commit()
        self.session.refresh(new_purchase)

        return new_purchase.as_resource()


    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        return self.session.query(PurchaseMySQLEntity).filter_by(cars_id=car_resource.id).first() is not None

# Placeholder for future repositories
# class OtherDBPurchaseRepository(PurchaseRepository):
#     ...