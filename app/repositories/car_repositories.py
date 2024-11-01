# External Library imports
from datetime import date
from sqlalchemy import exists
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List, Optional, cast
from sqlalchemy.exc import SQLAlchemyError


# Internal library imports
from app.models.purchase import Purchase
from app.models.car import Car, cars_has_accessories, cars_has_insurances
from app.resources.car_resource import (
    CarCreateResource,
    CarReturnResource,
    CustomerReturnResource,
    SalesPersonReturnResource,
    ModelReturnResource,
    ColorReturnResource,
    AccessoryReturnResource,
    InsuranceReturnResource
)





def calculate_total_price_for_car(
        model_resource: ModelReturnResource,
        color_resource: ColorReturnResource,
        accessory_resources: List[AccessoryReturnResource],
        insurance_resources: List[InsuranceReturnResource]) -> float:
    total_price: float = 0.0
    total_price += model_resource.price + color_resource.price
    for accessory_resource in accessory_resources:
        total_price += accessory_resource.price
    for insurance_resource in insurance_resources:
        total_price += insurance_resource.price
    if total_price < 0:
        total_price = 0.0
    return total_price


class CarRepository(ABC):

    @abstractmethod
    def get_all(
            self,
            customer: Optional[CustomerReturnResource] = None,
            sales_person: Optional[SalesPersonReturnResource] = None,
            is_purchased: Optional[bool] = None,
            is_past_purchase_deadline: Optional[bool] = None) -> List[CarReturnResource]:
        pass


    @abstractmethod
    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        pass

    @abstractmethod
    def create(
            self,
            car_create_data: CarCreateResource,
            customer_resource: CustomerReturnResource,
            sales_person_resource: SalesPersonReturnResource,
            model_resource: ModelReturnResource,
            color_resource: ColorReturnResource,
            accessory_resources: List[AccessoryReturnResource],
            insurance_resources: List[InsuranceReturnResource]) -> CarReturnResource:
        pass

class MySQLCarRepository(CarRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self,
            customer: Optional[CustomerReturnResource] = None,
            sales_person: Optional[SalesPersonReturnResource] = None,
            is_purchased: Optional[bool] = None,
            is_past_purchase_deadline: Optional[bool] = None) -> List[CarReturnResource]:

        car_query = self.session.query(Car)
        if customer is not None and isinstance(customer, CustomerReturnResource):
            car_query = car_query.filter_by(customers_id=customer.id)
        if sales_person is not None and isinstance(sales_person, SalesPersonReturnResource):
            car_query = car_query.filter_by(sales_people_id=sales_person.id)
        if is_purchased is not None and isinstance(is_purchased, bool):
            if is_purchased:
                car_query = car_query.filter(
                    exists().where(Purchase.cars_id == Car.id)
                )
            else:
                car_query = car_query.filter(
                    ~exists().where(Purchase.cars_id == Car.id)
                )
        if is_past_purchase_deadline is not None and isinstance(is_past_purchase_deadline, bool):
            current_date = date.today()
            if is_past_purchase_deadline:
                car_query = car_query.filter(Car.purchase_deadline < current_date)
            else:
                car_query = car_query.filter(Car.purchase_deadline >= current_date)

        cars: List[Car] = cast(List[Car], car_query.all())
        return [car.as_resource() for car in cars]


    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        car: Optional[Car] = self.session.query(Car).get(car_id)
        if car is not None:
            return car.as_resource()
        return None


    def create(self,
            car_create_data: CarCreateResource,
            customer_resource: CustomerReturnResource,
            sales_person_resource: SalesPersonReturnResource,
            model_resource: ModelReturnResource,
            color_resource: ColorReturnResource,
            accessory_resources: List[AccessoryReturnResource],
            insurance_resources: List[InsuranceReturnResource]) -> CarReturnResource:

        customer_id: str = customer_resource.id
        sales_person_id: str = sales_person_resource.id
        model_id: str = model_resource.id
        color_id: str = color_resource.id

        total_price: float = calculate_total_price_for_car(
            model_resource,
            color_resource,
            accessory_resources,
            insurance_resources)

        try:

            new_car = Car(
                models_id=model_id,
                colors_id=color_id,
                customers_id=customer_id,
                sales_people_id=sales_person_id,
                total_price=total_price,
                purchase_deadline=car_create_data.purchase_deadline
            )

            self.session.add(new_car)
            self.session.flush()

            for accessory_resource in accessory_resources:
                insert = cars_has_accessories.insert(
                ).values(cars_id=new_car.id, accessories_id=accessory_resource.id)
                self.session.execute(insert)

            for insurance_resource in insurance_resources:
                insert = cars_has_insurances.insert(
                ).values(cars_id=new_car.id, insurances_id=insurance_resource.id)
                self.session.execute(insert)


            self.session.commit()
            self.session.refresh(new_car)
            return new_car.as_resource()
        except Exception as e:
            self.session.rollback()
            raise SQLAlchemyError(f"{e}")


# Placeholder for future repositories
# class OtherDBCarRepository(CarRepository):
#     ...