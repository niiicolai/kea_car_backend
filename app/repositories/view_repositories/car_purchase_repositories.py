# External Library imports
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from typing import List, cast

# Internal library imports
from app.models.views.car_purchase import CarPurchaseView

from app.resources.view_resources.car_purchase_resource import (
    CarPurchaseSalePersonReturnResource,
    CarPurchaseCustomerReturnResource,
    SalesPersonWithCarsReturnResource,
    CustomerWithCarsReturnResource,
    SalesPersonReturnResource,
    CustomerReturnResource
)

def create_sales_person_with_cars_resource(
    sales_person_resource: SalesPersonReturnResource,
    sale_person_cars: List[CarPurchaseSalePersonReturnResource]
) -> SalesPersonWithCarsReturnResource:

    if not isinstance(sales_person_resource, SalesPersonReturnResource):
        raise TypeError(f"sales_person_resource should be a SalesPersonReturnResource, not {type(sales_person_resource)}.")
    if not all(isinstance(car, CarPurchaseSalePersonReturnResource) for car in sale_person_cars):
        raise TypeError("Each item in sale_person_cars should be a CarPurchaseViewSalePersonReturnResource")

    return SalesPersonWithCarsReturnResource(
        id=sales_person_resource.id,
        email=sales_person_resource.email,
        first_name=sales_person_resource.first_name,
        last_name=sales_person_resource.last_name,
        cars=sale_person_cars
    )

def create_customer_with_cars_resource(
        customer_resource: CustomerReturnResource,
        customer_cars: List[CarPurchaseCustomerReturnResource]
) -> CustomerWithCarsReturnResource:

    if not isinstance(customer_resource, CustomerReturnResource):
        raise TypeError(f"customer_resource should be a CustomerReturnResource, not {type(customer_resource)}.")
    if not all(isinstance(car, CarPurchaseCustomerReturnResource) for car in customer_cars):
        raise TypeError("Each item in customer_cars should be a CarPurchaseViewCustomerReturnResource")

    return CustomerWithCarsReturnResource(
        id=customer_resource.id,
        email=customer_resource.email,
        phone_number=customer_resource.phone_number,
        first_name=customer_resource.first_name,
        last_name=customer_resource.last_name,
        address=customer_resource.address,
        cars=customer_cars
    )

class CarPurchaseRepository(ABC):
    @abstractmethod
    def get_sales_person_with_cars(self, sales_person_resource: SalesPersonReturnResource) -> SalesPersonWithCarsReturnResource:
        pass

    @abstractmethod
    def get_customer_with_cars(self, customer_resource: CustomerReturnResource) -> CustomerWithCarsReturnResource:
        pass

class MySQLCarPurchaseRepository(CarPurchaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_sales_person_with_cars(self, sales_person_resource: SalesPersonReturnResource) -> SalesPersonWithCarsReturnResource:
        if not isinstance(sales_person_resource, SalesPersonReturnResource):
            raise TypeError(f"sales_person_resource should be a SalesPersonReturnResource, not {type(sales_person_resource)}.")

        car_purchase_sales_person_query = self.session.query(CarPurchaseView).filter_by(sales_person_id=sales_person_resource.id)

        sales_person_cars: List[CarPurchaseView] = cast(List[CarPurchaseView], car_purchase_sales_person_query.all())

        return create_sales_person_with_cars_resource(
            sales_person_resource,
            sale_person_cars=[sales_person_car.as_sales_person_resource() for sales_person_car in sales_person_cars]
        )

    def get_customer_with_cars(self, customer_resource: CustomerReturnResource) -> CustomerWithCarsReturnResource:
        if not isinstance(customer_resource, CustomerReturnResource):
            raise TypeError(f"customer_resource should be a CustomerReturnResource, not {type(customer_resource)}.")

        car_purchase_customer_query = self.session.query(CarPurchaseView).filter_by(customer_id=customer_resource.id)

        customer_cars: List[CarPurchaseView] = cast(List[CarPurchaseView], car_purchase_customer_query.all())

        return create_customer_with_cars_resource(
            customer_resource,
            customer_cars=[customer_car.as_customer_resource() for customer_car in customer_cars]
        )


