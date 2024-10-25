# External Library imports
from datetime import date
from typing import List, Optional


# Internal library imports
from app.repositories.car_repositories import CarRepository, CarReturnResource
from app.repositories.purchase_repositories import PurchaseRepository, PurchaseReturnResource, PurchaseCreateResource
from app.exceptions.database_errors import (
    UnableToFindIdError,
    PurchaseDeadlineHasPastError,
    AlreadyTakenFieldValueError,
    UnableToFindEntityError
)




def get_all(repository: PurchaseRepository) -> List[PurchaseReturnResource]:
    return repository.get_all()

def get_by_id(repository: PurchaseRepository, purchase_id: str) -> PurchaseReturnResource:
    purchase = repository.get_by_id(purchase_id)
    if purchase is None:
        raise UnableToFindIdError(entity_name="Purchase", entity_id=purchase_id)
    return purchase

def get_by_car_id(repository: PurchaseRepository, car_repository: CarRepository, car_id: str) -> PurchaseReturnResource:
    car: Optional[CarReturnResource] = car_repository.get_by_id(car_id)
    if car is None:
        raise UnableToFindIdError(entity_name="Car", entity_id=car_id)
    purchase: Optional[PurchaseReturnResource] = repository.get_by_car_id(car)
    if purchase is None:
        raise UnableToFindEntityError("Purchase", "cars_id", car_id)
    return purchase

def create(purchase_repository: PurchaseRepository, car_repository: CarRepository, purchase_create_data: PurchaseCreateResource) -> PurchaseReturnResource:
    car_id: str = str(purchase_create_data.cars_id)
    car: Optional[CarReturnResource] = car_repository.get_by_id(car_id)
    if car is None:
        raise UnableToFindIdError(entity_name="Car", entity_id=car_id)
    if purchase_repository.is_car_taken(car):
        raise AlreadyTakenFieldValueError(entity_name="Purchase", field="cars_id", value=car_id)
    if car.purchase_deadline < date.today():
        raise PurchaseDeadlineHasPastError(car)
    return purchase_repository.create(car)