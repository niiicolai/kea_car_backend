# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from pymongo.database import Database
from sqlalchemy.orm import Session

# Internal library imports
from app.models.car import prepare_car
from app.models.purchase import PurchaseReturnResource, PurchaseMySQLEntity, PurchaseMongoEntity
from app.resources.purchase_resource import PurchaseCreateResource, CarReturnResource


class PurchaseRepository(ABC):  # pragma: no cover

    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[PurchaseReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        pass

    @abstractmethod
    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        pass

    @abstractmethod
    def create(
            self,
            purchase_create_data: PurchaseCreateResource,
            car_resource: CarReturnResource
    ) -> PurchaseReturnResource:
        pass

    @abstractmethod
    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        pass


class MySQLPurchaseRepository(PurchaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[PurchaseReturnResource]:
        purchases_query = self.session.query(PurchaseMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            purchases_query = purchases_query.limit(limit)
        purchases: List[PurchaseMySQLEntity] = cast(List[PurchaseMySQLEntity], purchases_query.all())
        return [purchase.as_resource() for purchase in purchases]

    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        purchase: Optional[PurchaseMySQLEntity] = self.session.get(PurchaseMySQLEntity, purchase_id)
        if purchase is not None:
            return purchase.as_resource()
        return None

    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        purchase: Optional[PurchaseMySQLEntity] = self.session.query(PurchaseMySQLEntity).filter_by(
            cars_id=car_resource.id).first()
        if purchase is not None:
            return purchase.as_resource()
        return None

    def create(self, purchase_create_data: PurchaseCreateResource,
               car_resource: CarReturnResource) -> PurchaseReturnResource:
        new_purchase = PurchaseMySQLEntity(
            cars_id=car_resource.id,
            date_of_purchase=purchase_create_data.date_of_purchase
        )
        self.session.add(new_purchase)
        self.session.flush()
        self.session.refresh(new_purchase)

        return new_purchase.as_resource()

    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        return self.session.query(PurchaseMySQLEntity).filter_by(cars_id=car_resource.id).first() is not None


class MongoDBPurchaseRepository(PurchaseRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database


    def get_all(self, limit: Optional[int] = None) -> List[PurchaseReturnResource]:
        purchases_query = self.database.get_collection("purchases").find()
        if limit is not None and isinstance(limit, int) and limit > 0:
            purchases_query = purchases_query.limit(limit)

        purchases: List[PurchaseReturnResource] = []

        for purchase in purchases_query:
            car_entity = prepare_car(self.database, purchase.get("car"))
            purchases.append(
                PurchaseMongoEntity(
                    id=purchase.get("_id"),
                    car=car_entity,
                    date_of_purchase=purchase.get("date_of_purchase")
                ).as_resource()
            )
        return purchases

    def get_by_id(self, purchase_id: str) -> Optional[PurchaseReturnResource]:
        purchase = self.database.get_collection("purchases").find_one({"_id": purchase_id})
        if purchase is None:
            return None

        car_entity = prepare_car(self.database, purchase.get("car"))

        return PurchaseMongoEntity(
            _id=purchase.get("_id"),
            car=car_entity,
            date_of_purchase=purchase.get("date_of_purchase")
        ).as_resource()

    def get_by_car_id(self, car_resource: CarReturnResource) -> Optional[PurchaseReturnResource]:
        purchase = self.database.get_collection("purchases").find_one({"car._id": car_resource.id})
        if purchase is None:
            return None

        car_entity = prepare_car(self.database, purchase.get("car"))

        return PurchaseMongoEntity(
            id=purchase.get("_id"),
            car=car_entity,
            date_of_purchase=purchase.get("date_of_purchase")
        ).as_resource()

    def create(
            self,
            purchase_create_data: PurchaseCreateResource,
            car_resource: CarReturnResource
    ) -> PurchaseReturnResource:
        car_entity = prepare_car(self.database, car_resource)
        new_purchase = PurchaseMongoEntity(
            car=car_entity,
            date_of_purchase=purchase_create_data.date_of_purchase
        )
        self.database.get_collection("purchases").insert_one(new_purchase.model_dump(by_alias=True))
        return new_purchase.as_resource()

    def is_car_taken(self, car_resource: CarReturnResource) -> bool:
        return self.database.get_collection("purchases").count_documents({"car._id": car_resource.id}) > 0

# Placeholder for future repositories
# class OtherDBPurchaseRepository(PurchaseRepository):
#     ...
