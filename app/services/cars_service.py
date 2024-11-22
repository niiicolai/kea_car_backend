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
        cars_limit: Optional[int] = None
) -> List[CarReturnResource]:

    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, "
                        f"not {type(car_repository).__name__}.")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository must be of type CustomerRepository, "
                        f"not {type(customer_repository).__name__}.")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository must be of type SalesPersonRepository, "
                        f"not {type(sales_person_repository).__name__}.")

    if not (isinstance(customer_id, str) or customer_id is None):
        raise TypeError(f"customer_id must be of type str or None, "
                        f"not {type(customer_id).__name__}.")
    if not (isinstance(sales_person_id, str) or sales_person_id is None):
        raise TypeError(f"sales_person_id must be of type str or None, "
                        f"not {type(sales_person_id).__name__}.")

    if not (isinstance(is_purchased, bool) or is_purchased is None):
        raise TypeError(f"is_purchased must be of type bool or None, "
                        f"not {type(is_purchased).__name__}.")
    if not (isinstance(is_past_purchase_deadline, bool) or is_past_purchase_deadline is None):
        raise TypeError(f"is_past_purchase_deadline must be of type bool or None, "
                        f"not {type(is_past_purchase_deadline).__name__}.")
    if not (isinstance(cars_limit, int) or cars_limit is None):
        raise TypeError(f"cars_limit must be of type int or None, "
                        f"not {type(cars_limit).__name__}.")

    customer_resource: Optional[CustomerReturnResource] = None
    if customer_id is not None:
        customer_resource = customer_repository.get_by_id(customer_id)
        if customer_resource is None:
            raise UnableToFindIdError(
                entity_name="Customer",
                entity_id=customer_id
            )
    sales_person_resource = None
    if sales_person_id is not None:
        sales_person_resource = sales_person_repository.get_by_id(sales_person_id)
        if sales_person_resource is None:
            raise UnableToFindIdError(
                entity_name="Sales Person",
                entity_id=sales_person_id
            )

    return car_repository.get_all(
        customer=customer_resource,
        sales_person=sales_person_resource,
        is_purchased=is_purchased,
        is_past_purchase_deadline=is_past_purchase_deadline,
        limit=cars_limit
    )

def get_by_id(
        repository: CarRepository, car_id: str
) -> Optional[CarReturnResource]:

    if not isinstance(repository, CarRepository):
        raise TypeError(f"repository must be of type CarRepository, "
                        f"not {type(repository).__name__}.")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, "
                        f"not {type(car_id).__name__}.")

    car_resource = repository.get_by_id(car_id)
    if car_resource is None:
        raise UnableToFindIdError(
            entity_name="Car",
            entity_id=car_id
        )
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
        raise TypeError(f"car_repository must be of type CarRepository, "
                        f"not {type(car_repository).__name__}.")
    if not isinstance(customer_repository, CustomerRepository):
        raise TypeError(f"customer_repository must be of type CustomerRepository, "
                        f"not {type(customer_repository).__name__}.")
    if not isinstance(sales_person_repository, SalesPersonRepository):
        raise TypeError(f"sales_person_repository must be of type SalesPersonRepository, "
                        f"not {type(sales_person_repository).__name__}.")
    if not isinstance(model_repository, ModelRepository):
        raise TypeError(f"model_repository must be of type ModelRepository, "
                        f"not {type(model_repository).__name__}.")
    if not isinstance(color_repository, ColorRepository):
        raise TypeError(f"color_repository must be of type ColorRepository, "
                        f"not {type(color_repository).__name__}.")
    if not isinstance(accessory_repository, AccessoryRepository):
        raise TypeError(f"accessory_repository must be of type AccessoryRepository, "
                        f"not {type(accessory_repository).__name__}.")
    if not isinstance(insurance_repository, InsuranceRepository):
        raise TypeError(f"insurance_repository must be of type InsuranceRepository, "
                        f"not {type(insurance_repository).__name__}.")
    if not isinstance(car_create_data, CarCreateResource):
        raise TypeError(f"car_create_data must be of type CarCreateResource, "
                        f"not {type(car_create_data).__name__}.")

    customer_resource = customer_repository.get_by_id(str(car_create_data.customers_id))
    if customer_resource is None:
        raise UnableToFindIdError("Customer", car_create_data.customers_id)

    sales_person_resource: Optional[SalesPersonReturnResource] = sales_person_repository.get_by_id(str(car_create_data.sales_people_id))
    if sales_person_resource is None:
        raise UnableToFindIdError("Sales Person", car_create_data.sales_people_id)

    model_resource: Optional[ModelReturnResource] = model_repository.get_by_id(str(car_create_data.models_id))
    if model_resource is None:
        raise UnableToFindIdError("Model", car_create_data.models_id)

    color_resource: Optional[ColorReturnResource] = color_repository.get_by_id(str(car_create_data.colors_id))
    if color_resource is None:
        raise UnableToFindIdError("Color", car_create_data.colors_id)

    if str(car_create_data.colors_id) not in [color.id for color in model_resource.colors]:
        raise TheColorIsNotAvailableInModelToGiveToCarError(model_resource, color_resource)

    accessory_resources: List[AccessoryReturnResource] = []
    for accessory_uuid in car_create_data.accessory_ids:
        accessory: Optional[AccessoryReturnResource] = (accessory_repository
                                                        .get_by_id(str(accessory_uuid)))
        if accessory is None:
            raise UnableToFindIdError(
                entity_name="Accessory",
                entity_id=accessory_uuid
            )
        accessory_resources.append(accessory)

    insurance_resources: List[InsuranceReturnResource] = []
    for insurance_uuid in car_create_data.insurance_ids:
        insurance: Optional[InsuranceReturnResource] = insurance_repository.get_by_id(str(insurance_uuid))
        if insurance is None:
            raise UnableToFindIdError(
                entity_name="Insurance",
                entity_id=insurance_uuid
            )
        insurance_resources.append(insurance)

    return car_repository.create(
        car_create_data,
        customer_resource,
        sales_person_resource,
        model_resource,
        color_resource,
        accessory_resources,
        insurance_resources)

def delete(
        car_repository: CarRepository,
        purchase_repository: PurchaseRepository,
        car_id: str, delete_purchase_too: bool
) -> None:

    if not isinstance(car_repository, CarRepository):
        raise TypeError(f"car_repository must be of type CarRepository, "
                        f"not {type(car_repository).__name__}.")
    if not isinstance(purchase_repository, PurchaseRepository):
        raise TypeError(f"purchase_repository must be of type PurchaseRepository, "
                        f"not {type(purchase_repository).__name__}.")
    if not isinstance(car_id, str):
        raise TypeError(f"car_id must be of type str, "
                        f"not {type(car_id).__name__}.")
    if not isinstance(delete_purchase_too, bool):
        raise TypeError(f"delete_purchase_too must be of type bool, "
                        f"not {type(delete_purchase_too).__name__}.")

    car_resource = car_repository.get_by_id(car_id)
    if car_resource is None:
        raise UnableToFindIdError(
            entity_name="Car",
            entity_id=car_id
        )
    car_has_purchase = purchase_repository.is_car_taken(car_resource)
    if car_has_purchase and not delete_purchase_too:
        raise UnableToDeleteCarWithoutDeletingPurchaseTooError(car_resource)

    car_repository.delete(car_resource, delete_purchase_too)
