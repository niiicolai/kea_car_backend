from typing import Optional, List

from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.customer_repositories import CustomerRepository
from app.repositories.sales_person_repositories import SalesPersonRepository

from app.repositories.view_repositories.car_purchase_repositories import (
    CarPurchaseRepository,
    CarPurchaseReturnResource,
    CustomerWithCarsReturnResource,
    SalesPersonWithCarsReturnResource
)

def get_sales_person_with_cars(
        car_purchase_repository: CarPurchaseRepository,
        sales_person_repository: SalesPersonRepository,
        sales_person_id: str
) -> SalesPersonWithCarsReturnResource:

    if not isinstance(car_purchase_repository, CarPurchaseRepository):
        raise TypeError(f"car_purchase_repository must be of type CarPurchaseViewRepository, "
                        f"not {type(car_purchase_repository).__name__}.")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository must be of type SalesPersonRepository, "
                        f"not {type(sales_person_repository).__name__}.")
    if not isinstance(sales_person_id, str):
        raise TypeError(f"sales_person_id must be of type str, "
                        f"not {type(sales_person_id).__name__}.")

    sales_person_resource = sales_person_repository.get_by_id(sales_person_id)
    if sales_person_resource is None:
        raise UnableToFindIdError(
            entity_name="Sales Person",
            entity_id=sales_person_id
        )

    return car_purchase_repository.get_sales_person_with_cars(sales_person_resource)

def get_customer_with_cars(
        car_purchase_repository: CarPurchaseRepository,
        customer_repository: CustomerRepository,
        customer_id: str
) -> CustomerWithCarsReturnResource:

    if not isinstance(car_purchase_repository, CarPurchaseRepository):
        raise TypeError(f"car_purchase_repository must be of type CarPurchaseViewRepository, "
                        f"not {type(car_purchase_repository).__name__}.")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository must be of type CustomerRepository, "
                        f"not {type(customer_repository).__name__}.")
    if not isinstance(customer_id, str):
        raise TypeError(f"customer_id must be of type str, "
                        f"not {type(customer_id).__name__}.")

    customer_resource = customer_repository.get_by_id(customer_id)
    if customer_resource is None:
        raise UnableToFindIdError(
            entity_name="Customer",
            entity_id=customer_id
        )

    return car_purchase_repository.get_customer_with_cars(customer_resource)

def get_cars_with_purchase(
        repository: CarPurchaseRepository,
        cars_purchase_limit: Optional[int] = None
) -> List[CarPurchaseReturnResource]:
    if not isinstance(repository, CarPurchaseRepository):
        raise TypeError(f"repository must be of type CarPurchaseRepository, "
                        f"not {type(repository).__name__}.")
    if not (isinstance(cars_purchase_limit, int) or cars_purchase_limit is None):
        raise TypeError(f"cars_purchase_limit must be of type int or None, "
                        f"not {type(cars_purchase_limit).__name__}.")

    return repository.get_cars_with_purchase(cars_purchase_limit)

def get_car_with_purchase_by_id(
        repository: CarPurchaseRepository,
        car_id: str
) -> CarPurchaseReturnResource:
    if not isinstance(repository, CarPurchaseRepository):
        raise TypeError(f"repository must be of type CarPurchaseRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, "
                        f"not {type(car_id).__name__}.")

    car_purchase_resource = repository.get_car_with_purchase_by_id(car_id)
    if car_purchase_resource is None:
        raise UnableToFindIdError("Car", car_id)
    return car_purchase_resource

