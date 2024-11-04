# External Library imports
from typing import List, Optional

# Internal library imports
from app.repositories.model_repositories import ModelRepository, ModelReturnResource
from app.repositories.color_repositories import ColorRepository, ColorReturnResource
from app.repositories.purchase_repositories import PurchaseRepository, PurchaseReturnResource
from app.repositories.customer_repositories import CustomerRepository, CustomerReturnResource
from app.repositories.insurance_repository import InsuranceRepository, InsuranceReturnResource
from app.repositories.accessory_repositories import AccessoryRepository, AccessoryReturnResource
from app.repositories.car_repositories import CarRepository, CarReturnResource, CarCreateResource
from app.repositories.sales_person_repositories import SalesPersonRepository, SalesPersonReturnResource
from app.exceptions.database_errors import UnableToFindIdError, TheColorIsNotAvailableInModelToGiveToCarError, UnableToDeleteCarWithoutDeletingPurchaseTooError

def get_all(
        car_repository: CarRepository,
        customer_repository: CustomerRepository,
        sales_person_repository: SalesPersonRepository,
        customer_id: Optional[str] = None,
        sales_person_id: Optional[str] = None,
        is_purchased: Optional[bool] = None,
        is_past_purchase_deadline: Optional[bool] = None,
        cars_limit: Optional[int] = None) -> List[CarReturnResource]:

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

def delete(car_repository: CarRepository, purchase_repository: PurchaseRepository, car_id: str, delete_purchase_too: bool) -> CarReturnResource:
    car_resource = car_repository.get_by_id(car_id)
    if car_resource is None:
        raise UnableToFindIdError("Car", car_id)
    car_has_purchase = purchase_repository.is_car_taken(car_resource)
    if car_has_purchase and not delete_purchase_too:
        raise UnableToDeleteCarWithoutDeletingPurchaseTooError(car_resource)

    return car_repository.delete(car_resource, delete_purchase_too)