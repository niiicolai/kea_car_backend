# External Library imports
from datetime import date
from typing import List, Optional


# Internal library imports
from app.repositories.car_repositories import CarRepository, CarReturnResource
from app.repositories.purchase_repositories import (
    PurchaseRepository,
    PurchaseReturnResource,
    PurchaseCreateResource
)
from app.exceptions.database_errors import (
    PurchaseDeadlineHasPastError,
    AlreadyTakenFieldValueError,
    UnableToFindEntityError,
    UnableToFindIdError
)


def get_all(
        repository: PurchaseRepository,
        purchases_limit: Optional[int] = None
)  -> List[PurchaseReturnResource]:

    if not isinstance(repository, PurchaseRepository):
        raise TypeError(f"repository must be of type PurchaseRepository, "
                        f"not {type(repository).__name__}.")
    if not (isinstance(purchases_limit, int) or purchases_limit is None):
        raise TypeError(f"purchases_limit must be of type int or None, "
                        f"not {type(purchases_limit).__name__}.")

    return repository.get_all(limit=purchases_limit)

def get_by_id(
        repository: PurchaseRepository,
        purchase_id: str
) -> PurchaseReturnResource:

    if not isinstance(repository, PurchaseRepository):
        raise TypeError(f"repository must be of type PurchaseRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(purchase_id, str):
        raise TypeError(f"purchase_id must be of type str, "
                        f"not {type(purchase_id).__name__}.")

    purchase = repository.get_by_id(purchase_id)
    if purchase is None:
        raise UnableToFindIdError(
            entity_name="Purchase",
            entity_id=purchase_id
        )

    return purchase

def get_by_car_id(
        purchase_repository: PurchaseRepository,
        car_repository: CarRepository,
        car_id: str
) -> PurchaseReturnResource:

    if not isinstance(purchase_repository, PurchaseRepository):
        raise TypeError(f"purchase_repository must be of type PurchaseRepository, "
                        f"not {type(purchase_repository).__name__}.")
    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, "
                        f"not {type(car_repository).__name__}.")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, "
                        f"not {type(car_id).__name__}.")

    car = car_repository.get_by_id(car_id)
    if car is None:
        raise UnableToFindIdError(
            entity_name="Car",
            entity_id=car_id
        )

    purchase = purchase_repository.get_by_car_id(car)
    if purchase is None:
        raise UnableToFindEntityError(
            entity_name="Purchase",
            field="cars_id",
            value=car_id
        )

    return purchase

def create(
        purchase_repository: PurchaseRepository,
        car_repository: CarRepository,
        purchase_create_data: PurchaseCreateResource
) -> PurchaseReturnResource:

    if not isinstance(purchase_repository, PurchaseRepository):
        raise TypeError(f"purchase_repository must be of type PurchaseRepository, "
                        f"not {type(purchase_repository).__name__}.")
    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, "
                        f"not {type(car_repository).__name__}.")
    if not isinstance(purchase_create_data, PurchaseCreateResource):
        raise TypeError(f"purchase_create_data must be of type PurchaseCreateResource, "
                        f"not {type(purchase_create_data).__name__}.")

    car_id: str = str(purchase_create_data.cars_id)
    car = car_repository.get_by_id(car_id)
    if car is None:
        raise UnableToFindIdError(
            entity_name="Car",
            entity_id=car_id
        )

    if purchase_repository.is_car_taken(car):
        raise AlreadyTakenFieldValueError(
            entity_name="Purchase",
            field="cars_id",
            value=car_id
        )

    date_of_purchase: date = purchase_create_data.date_of_purchase
    if car.purchase_deadline < date_of_purchase:
        raise PurchaseDeadlineHasPastError(car, date_of_purchase)

    return purchase_repository.create(
        purchase_create_data=purchase_create_data,
        car_resource=car
    )
