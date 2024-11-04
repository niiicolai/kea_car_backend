# External Library imports
from datetime import date
from sqlalchemy import text, exists
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.exc import SQLAlchemyError

# Internal library imports
from app.models.purchase import PurchaseMySQLEntity
from app.models.car import CarReturnResource, CarMySQLEntity, cars_has_accessories, cars_has_insurances
from app.resources.car_resource import (
    CarCreateResource,
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
            customer: Optional[CustomerReturnResource],
            sales_person: Optional[SalesPersonReturnResource],
            is_purchased: Optional[bool],
            is_past_purchase_deadline: Optional[bool],
            limit: Optional[int]) -> List[CarReturnResource]:
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

    @abstractmethod
    def delete(self, car_resource: CarReturnResource, delete_purchase_too: bool) -> CarReturnResource:
        pass


class MySQLCarRepository(CarRepository):
    def __init__(self, session: Session):
        self.session = session

    # This is the past function for get_all,that now uses a stored procedure to handle the logic of filtering all the cars to get
    def get_all_past_function(self,
                              customer: Optional[CustomerReturnResource],
                              sales_person: Optional[SalesPersonReturnResource],
                              is_purchased: Optional[bool],
                              is_past_purchase_deadline: Optional[bool],
                              limit: Optional[int]) -> List[CarReturnResource]:

        car_query = self.session.query(CarMySQLEntity)
        if customer is not None and isinstance(customer, CustomerReturnResource):
            car_query = car_query.filter_by(customers_id=customer.id)
        if sales_person is not None and isinstance(sales_person, SalesPersonReturnResource):
            car_query = car_query.filter_by(sales_people_id=sales_person.id)
        if is_purchased is not None and isinstance(is_purchased, bool):
            if is_purchased:
                car_query = car_query.filter(
                    exists().where(PurchaseMySQLEntity.cars_id == CarMySQLEntity.id)
                )
            else:
                car_query = car_query.filter(
                    ~exists().where(PurchaseMySQLEntity.cars_id == CarMySQLEntity.id)
                )
        if is_past_purchase_deadline is not None and isinstance(is_past_purchase_deadline, bool):
            current_date = date.today()
            if is_past_purchase_deadline:
                car_query = car_query.filter(CarMySQLEntity.purchase_deadline < current_date)
            else:
                car_query = car_query.filter(CarMySQLEntity.purchase_deadline >= current_date)

        if limit is not None and isinstance(limit, int) and limit > 0:
            car_query = car_query.limit(limit)

        cars: List[CarMySQLEntity] = cast(List[CarMySQLEntity], car_query.all())
        return [car.as_resource() for car in cars]

    def get_all(self,
                customer: Optional[CustomerReturnResource],
                sales_person: Optional[SalesPersonReturnResource],
                is_purchased: Optional[bool],
                is_past_purchase_deadline: Optional[bool],
                limit: Optional[int]) -> List[CarReturnResource]:

        # Define parameters
        customer_id = customer.id if customer else None
        sales_person_id = sales_person.id if sales_person else None

        cars_result = self.session.execute(
            text("""
                        CALL get_all_cars(
                            :p_customer_id,
                            :p_sales_person_id,
                            :p_is_purchased,
                            :p_is_past_purchase_deadline,
                            :p_current_date,
                            :p_limit
                        );
                    """),
            {
                "p_customer_id": customer_id,
                "p_sales_person_id": sales_person_id,
                "p_is_purchased": is_purchased,
                "p_is_past_purchase_deadline": is_past_purchase_deadline,
                "p_current_date": date.today(),
                "p_limit": limit
            }
        ).fetchall()

        cars: List[CarMySQLEntity] = []
        for car_result in cars_result:
            # Construct the dictionary directly
            car_id: str = car_result[0]
            if not isinstance(car_id, str):
                raise SQLAlchemyError(f"The car_id '{car_id}' was not a string but a '{type(car_id).__name__}'.")
            car = self.session.get(CarMySQLEntity, car_id)
            if car is None:
                raise SQLAlchemyError(f"The car with id: '{car_id}' did not exist in the database.")
            car = cast(CarMySQLEntity, car)
            cars.append(car)
        return [car.as_resource() for car in cars]

    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        car: Optional[CarMySQLEntity] = self.session.query(CarMySQLEntity).get(car_id)
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

            new_car = CarMySQLEntity(
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

    def delete(self, car_resource: CarReturnResource, delete_purchase_too: bool) -> CarReturnResource:
        try:
            if delete_purchase_too:
                self.session.query(PurchaseMySQLEntity).filter_by(cars_id=car_resource.id).delete()
                self.session.flush()
            self.session.query(CarMySQLEntity).filter_by(id=car_resource.id).delete()
            self.session.commit()
            return car_resource
        except Exception as e:
            self.session.rollback()
            raise SQLAlchemyError(f"{e}")

# Placeholder for future repositories
# class OtherDBCarRepository(CarRepository):
#     ...
