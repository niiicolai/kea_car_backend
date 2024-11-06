# External Library imports
from typing import List, Optional

# Internal library imports
from app.repositories.purchase_repositories import PurchaseRepository
from app.repositories.model_repositories import ModelRepository, ModelReturnResource
from app.repositories.color_repositories import ColorRepository, ColorReturnResource
from app.repositories.customer_repositories import CustomerRepository, CustomerReturnResource
from app.repositories.insurance_repository import InsuranceRepository, InsuranceReturnResource
from app.repositories.accessory_repositories import AccessoryRepository, AccessoryReturnResource
from app.repositories.car_repositories import CarRepository, CarReturnResource, CarCreateResource
from app.repositories.sales_person_repositories import SalesPersonRepository, SalesPersonReturnResource
from app.exceptions.database_errors import (
    UnableToFindIdError,
    TheColorIsNotAvailableInModelToGiveToCarError,
    UnableToDeleteCarWithoutDeletingPurchaseTooError
)

def get_all(
        car_repository: CarRepository,
        customer_repository: CustomerRepository,
        sales_person_repository: SalesPersonRepository,
        customer_id: Optional[str] = None,
        sales_person_id: Optional[str] = None,
        is_purchased: Optional[bool] = None,
        is_past_purchase_deadline: Optional[bool] = None,
        cars_limit: Optional[int] = None) -> List[CarReturnResource]:

    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, not {type(car_repository)}")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository must be of type CustomerRepository, not {type(customer_repository)}")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository must be of type SalesPersonRepository, not {type(sales_person_repository)}")

    if not (isinstance(customer_id, str) or customer_id is None):
        raise TypeError(f"customer_id must be of type str or None, not {type(customer_id)}")
    if not (isinstance(sales_person_id, str) or sales_person_id is None):
        raise TypeError(f"sales_person_id must be of type str or None, not {type(sales_person_id)}")

    if not (isinstance(is_purchased, bool) or is_purchased is None):
        raise TypeError(f"is_purchased must be of type bool or None, not {type(is_purchased)}")
    if not (isinstance(is_past_purchase_deadline, bool) or is_past_purchase_deadline is None):
        raise TypeError(f"is_past_purchase_deadline must be of type bool or None, not {type(is_past_purchase_deadline)}")
    if not (isinstance(cars_limit, int) or cars_limit is None):
        raise TypeError(f"cars_limit must be of type int or None, not {type(cars_limit)}")

    customer_resource: Optional[CustomerReturnResource] = None
    if customer_id is not None:
        customer_resource = customer_repository.get_by_id(customer_id)
        if customer_resource is None:
            raise UnableToFindIdError("Customer", customer_id)
    sales_person_resource: Optional[SalesPersonReturnResource] = None
    if sales_person_id is not None:
        sales_person_resource = sales_person_repository.get_by_id(sales_person_id)
        if sales_person_resource is None:
            raise UnableToFindIdError("Sales Person", sales_person_id)

    return car_repository.get_all(
        customer=customer_resource,
        sales_person=sales_person_resource,
        is_purchased=is_purchased,
        is_past_purchase_deadline=is_past_purchase_deadline,
        limit=cars_limit
    )

def get_by_id(repository: CarRepository, car_id: str) -> Optional[CarReturnResource]:
    if not isinstance(repository, CarRepository):
        raise TypeError(f"repository must be of type CarRepository, not {type(repository)}")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, not {type(car_id)}")

    car_resource: Optional[CarReturnResource] = repository.get_by_id(car_id)
    if car_resource is None:
        raise UnableToFindIdError("Car", car_id)
    return car_resource


def create(
        car_repository: CarRepository,
        customer_repository: CustomerRepository,
        sales_person_repository: SalesPersonRepository,
        model_repository: ModelRepository,
        color_repository: ColorRepository,
        accessory_repository: AccessoryRepository,
        insurance_repository: InsuranceRepository,
        car_create_data: CarCreateResource) -> CarReturnResource:

    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, not {type(car_repository)}")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository must be of type CustomerRepository, not {type(customer_repository)}")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository must be of type SalesPersonRepository, not {type(sales_person_repository)}")
    if not isinstance(model_repository, ModelRepository):
        raise TypeError(f"model_repository must be of type ModelRepository, not {type(model_repository)}")
    if not isinstance(color_repository, ColorRepository):
        raise TypeError(f"color_repository must be of type ColorRepository, not {type(color_repository)}")
    if not isinstance(accessory_repository, AccessoryRepository):
        raise TypeError(f"accessory_repository must be of type AccessoryRepository, not {type(accessory_repository)}")
    if not isinstance(insurance_repository, InsuranceRepository):
        raise TypeError(f"insurance_repository must be of type InsuranceRepository, not {type(insurance_repository)}")
    if not isinstance(car_create_data, CarCreateResource):
        raise TypeError(f"car_create_data must be of type CarCreateResource, not {type(car_create_data)}")

    customer_id = str(car_create_data.customers_id)
    customer_resource: Optional[CustomerReturnResource] = customer_repository.get_by_id(customer_id)
    if customer_resource is None:
        raise UnableToFindIdError("Customer", customer_id)

    sales_person_id = str(car_create_data.sales_people_id)
    sales_person_resource: Optional[SalesPersonReturnResource] = sales_person_repository.get_by_id(sales_person_id)
    if sales_person_resource is None:
        raise UnableToFindIdError("Sales Person", sales_person_id)

    model_id = str(car_create_data.models_id)
    model_resource: Optional[ModelReturnResource] = model_repository.get_by_id(model_id)
    if model_resource is None:
        raise UnableToFindIdError("Model", model_id)

    color_id = str(car_create_data.colors_id)
    color_resource: Optional[ColorReturnResource] = color_repository.get_by_id(color_id)
    if color_resource is None:
        raise UnableToFindIdError("Color", color_id)
    color_ids_within_model = [color.id for color in model_resource.colors]
    if color_id not in color_ids_within_model:
        raise TheColorIsNotAvailableInModelToGiveToCarError(model_resource, color_resource)

    accessory_resources: List[AccessoryReturnResource] = []
    for accessory_uuid in car_create_data.accessory_ids:
        accessory_id = str(accessory_uuid)
        accessory: Optional[AccessoryReturnResource] = accessory_repository.get_by_id(accessory_id)
        if accessory is None:
            raise UnableToFindIdError("Accessory", accessory_id)
        accessory_resources.append(accessory)

    insurance_resources: List[InsuranceReturnResource] = []
    for insurance_uuid in car_create_data.insurance_ids:
        insurance_id = str(insurance_uuid)
        insurance: Optional[InsuranceReturnResource] = insurance_repository.get_by_id(insurance_id)
        if insurance is None:
            raise UnableToFindIdError("Insurance", insurance_id)
        insurance_resources.append(insurance)

    return car_repository.create(
        car_create_data,
        customer_resource,
        sales_person_resource,
        model_resource,
        color_resource,
        accessory_resources,
        insurance_resources)

def delete(car_repository: CarRepository, purchase_repository: PurchaseRepository, car_id: str, delete_purchase_too: bool):
    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, not {type(car_repository)}")
    if not isinstance(purchase_repository, PurchaseRepository):
        raise TypeError(f"purchase_repository must be of type PurchaseRepository, not {type(purchase_repository)}")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, not {type(car_id)}")
    if not isinstance(delete_purchase_too, bool):
        raise TypeError(f"delete_purchase_too must be of type bool, not {type(delete_purchase_too)}")
    car_resource = car_repository.get_by_id(car_id)
    if car_resource is None:
        raise UnableToFindIdError("Car", car_id)
    car_has_purchase = purchase_repository.is_car_taken(car_resource)
    if car_has_purchase and not delete_purchase_too:
        raise UnableToDeleteCarWithoutDeletingPurchaseTooError(car_resource)

    car_repository.delete(car_resource, delete_purchase_too)