# External Library imports
from abc import ABC, abstractmethod
from typing import List, Optional, cast
from sqlalchemy.orm import Session

# Internal library imports
from app.models.views.car_purchase import CarPurchaseView

from app.resources.view_resources.car_purchase_resource import (
    CarPurchaseSalePersonReturnResource,
    CarPurchaseCustomerReturnResource,
    SalesPersonWithCarsReturnResource,
    CustomerWithCarsReturnResource,
    SalesPersonReturnResource,
    CarPurchaseReturnResource,
    CustomerReturnResource
)


def create_sales_person_with_cars_resource(
    sales_person_resource: SalesPersonReturnResource,
    sale_person_cars: List[CarPurchaseSalePersonReturnResource]
) -> SalesPersonWithCarsReturnResource:

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

    return CustomerWithCarsReturnResource(
        id=customer_resource.id,
        email=customer_resource.email,
        phone_number=customer_resource.phone_number,
        first_name=customer_resource.first_name,
        last_name=customer_resource.last_name,
        address=customer_resource.address,
        cars=customer_cars
    )


class CarPurchaseRepository(ABC):  # pragma: no cover
    @abstractmethod
    def get_sales_person_with_cars(
            self,
            sales_person_resource: SalesPersonReturnResource
    ) -> SalesPersonWithCarsReturnResource:
        pass

    @abstractmethod
    def get_customer_with_cars(
            self,
            customer_resource: CustomerReturnResource
    ) -> CustomerWithCarsReturnResource:
        pass

    @abstractmethod
    def get_cars_with_purchase(
            self,
            limit: Optional[int]
    ) -> List[CarPurchaseReturnResource]:
        pass

    @abstractmethod
    def get_car_with_purchase_by_id(
            self,
            car_id: str
    ) -> Optional[CarPurchaseReturnResource]:
        pass


class MySQLCarPurchaseRepository(CarPurchaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_sales_person_with_cars(
            self,
            sales_person_resource: SalesPersonReturnResource
    ) -> SalesPersonWithCarsReturnResource:

        car_purchase_sales_person_query = self.session.query(CarPurchaseView).filter_by(
            sales_person_id=sales_person_resource.id
        )

        sales_person_cars = cast(List[CarPurchaseView], car_purchase_sales_person_query.all())

        return create_sales_person_with_cars_resource(
            sales_person_resource,
            sale_person_cars=[sales_person_car.as_sales_person_resource() for sales_person_car in sales_person_cars]
        )

    def get_customer_with_cars(self, customer_resource: CustomerReturnResource) -> CustomerWithCarsReturnResource:

        car_purchase_customer_query = self.session.query(CarPurchaseView).filter_by(
            customer_id=customer_resource.id
        )

        customer_cars = cast(List[CarPurchaseView], car_purchase_customer_query.all())

        return create_customer_with_cars_resource(
            customer_resource,
            customer_cars=[customer_car.as_customer_resource() for customer_car in customer_cars]
        )

    def get_cars_with_purchase(self, limit: Optional[int]) -> List[CarPurchaseReturnResource]:
        cars_with_purchase_query = self.session.query(CarPurchaseView)

        if limit is not None and isinstance(limit, int) and limit > 0:
            cars_with_purchase_query = cars_with_purchase_query.limit(limit)

        cars_with_purchase = cast(List[CarPurchaseView], cars_with_purchase_query.all())

        return [car_with_purchase.as_resource() for car_with_purchase in cars_with_purchase]

    def get_car_with_purchase_by_id(self, car_id: str) -> Optional[CarPurchaseReturnResource]:
        car_with_purchase: Optional[CarPurchaseView] = self.session.query(CarPurchaseView).get(car_id)
        if car_with_purchase is not None:
            return car_with_purchase.as_resource()
        return None


# Placeholder for future repositories
# class OtherDBCustomerRepository(CustomerRepository):
#     ...
