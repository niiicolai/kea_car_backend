# External Library imports
from typing import List, Optional

# Internal library imports
from app.repositories.model_repositories import ModelRepository, ModelReturnResource
from app.repositories.color_repositories import ColorRepository, ColorReturnResource
from app.repositories.customer_repositories import CustomerRepository, CustomerReturnResource
from app.repositories.insurance_repository import InsuranceRepository, InsuranceReturnResource
from app.repositories.accessory_repositories import AccessoryRepository, AccessoryReturnResource
from app.repositories.car_repositories import CarRepository, CarReturnResource, CarCreateResource
from app.repositories.sales_person_repositories import SalesPersonRepository, SalesPersonReturnResource
from app.exceptions.database_errors import UnableToFindIdError, UnableToGiveEntityWithValueFromOtherEntityError

def get_all(
        car_repository: CarRepository,
        customer_repository: CustomerRepository,
        sales_person_repository: SalesPersonRepository,
        customer_id: Optional[str] = None,
        sales_person_id: Optional[str] = None) -> List[CarReturnResource]:
    filtering_by_customer: bool = customer_id is not None
    filtering_by_sales_person: bool = sales_person_id is not None

    if filtering_by_customer and filtering_by_sales_person:
        customer_resource: Optional[CustomerReturnResource] = customer_repository.get_by_id(customer_id)
        if customer_resource is None:
            raise UnableToFindIdError("Customer", customer_id)
        sales_person_resource: Optional[SalesPersonReturnResource] = sales_person_repository.get_by_id(sales_person_id)
        if sales_person_resource is None:
            raise UnableToFindIdError("Sales Person", sales_person_id)
        return car_repository.get_all_by_customer_and_sales_person_id(customer_resource, sales_person_resource)

    if filtering_by_customer:
        customer_resource: Optional[CustomerReturnResource] = customer_repository.get_by_id(customer_id)
        if customer_resource is None:
            raise UnableToFindIdError("Customer", customer_id)
        return car_repository.get_all_by_customer_id(customer_resource)

    if filtering_by_sales_person:
        sales_person_resource: Optional[SalesPersonReturnResource] = sales_person_repository.get_by_id(sales_person_id)
        if sales_person_resource is None:
            raise UnableToFindIdError("Sales Person", sales_person_id)
        return car_repository.get_all_by_sales_person_id(sales_person_resource)


    return car_repository.get_all()

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
        raise UnableToGiveEntityWithValueFromOtherEntityError("Car", "Color", color_resource.name, "Model")

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