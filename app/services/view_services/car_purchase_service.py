# External Library imports
from typing import Optional

# Internal library imports
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.customer_repositories import CustomerRepository
from app.repositories.sales_person_repositories import SalesPersonRepository

from app.repositories.view_repositories.car_purchase_repositories import (
    CarPurchaseRepository,
    CustomerReturnResource,
    SalesPersonReturnResource,
    CustomerWithCarsReturnResource,
    SalesPersonWithCarsReturnResource
)


def get_sales_person_with_cars(car_purchase_repository: CarPurchaseRepository, sales_person_repository: SalesPersonRepository, sales_person_id: str) -> SalesPersonWithCarsReturnResource:
    if not isinstance(car_purchase_repository, CarPurchaseRepository):
        raise TypeError(f"car_purchase_repository should be a CarPurchaseViewRepository and not {type(car_purchase_repository)}")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository should be a SalesPersonRepository and not {type(sales_person_repository)}")
    if not isinstance(sales_person_id, str):
        raise TypeError(f"sales_person_id should be a string and not {type(sales_person_id)}")

    sales_person_resource: Optional[SalesPersonReturnResource] = sales_person_repository.get_by_id(sales_person_id)
    if sales_person_resource is None:
        raise UnableToFindIdError(entity_name="Sales Person", entity_id=sales_person_id)

    return car_purchase_repository.get_sales_person_with_cars(sales_person_resource)

def get_customer_with_cars(car_purchase_repository: CarPurchaseRepository, customer_repository: CustomerRepository, customer_id: str) -> CustomerWithCarsReturnResource:
    if not isinstance(car_purchase_repository, CarPurchaseRepository):
        raise TypeError(f"car_purchase_repository should be a CarPurchaseViewRepository and not {type(car_purchase_repository)}")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository should be a CustomerRepository and not {type(customer_repository)}")
    if not isinstance(customer_id, str):
        raise TypeError(f"customer_id should be a string and not {type(customer_id)}")

    customer_resource: Optional[CustomerReturnResource] = customer_repository.get_by_id(customer_id)
    if customer_resource is None:
        raise UnableToFindIdError(entity_name="Customer", entity_id=customer_id)

    return car_purchase_repository.get_customer_with_cars(customer_resource)


