from pydantic import ValidationError

from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.models.accessory import Accessory
from app.models.car import Car
from app.models.customer import Customer
from app.models.insurance import Insurance
from app.models.sales_person import SalesPerson
from app.models.model import Model, Color
from sqlalchemy.orm import Session
from typing import List, Optional, cast

from app.resources.car_resource import CarCreateResource


def get_all(customer_id: Optional[str], sales_person_id: Optional[str], session: Session) -> List[Car]:
    filtering_by_customer: bool = customer_id is not None
    filtering_by_sales_person: bool = sales_person_id is not None

    if filtering_by_customer and session.query(Customer).get(customer_id) is None:
        raise UnableToFindIdError("Customer", customer_id)
    if filtering_by_sales_person and session.query(SalesPerson).get(sales_person_id) is None:
        raise UnableToFindIdError("Sales Person", sales_person_id)

    if filtering_by_customer and filtering_by_sales_person:
        cars = session.query(Car).filter_by(customers_id=customer_id, sales_people_id=sales_person_id).all()
    elif filtering_by_customer:
        cars = session.query(Car).filter_by(customers_id=customer_id).all()
    elif filtering_by_sales_person:
        cars = session.query(Car).filter_by(sales_people_id=sales_person_id).all()
    else:
        cars = session.query(Car).all()

    return cast(List[Car], cars)


def create(car_create_data: CarCreateResource, session: Session) -> Car:
    model_id = str(car_create_data.models_id)
    color_id = str(car_create_data.colors_id)
    customer_id = str(car_create_data.customers_id)
    sales_person_id = str(car_create_data.sales_people_id)

    model: Model = session.query(Model).get(model_id)

    if model is None:
        raise UnableToFindIdError("Model", car_create_data.models_id)
    model_price = model.price

    color: Color = session.query(Color).get(color_id)
    if color is None:
        raise UnableToFindIdError("Color", car_create_data.colors_id)

    model_color_ids = [model_color.id for model_color in model.colors]

    if color.id not in model_color_ids:
        raise ValidationError(f"The color id: '{color.id}' is not between the color ids: '{model_color_ids}', for the model with id: '{model.id}'.")
    color_price = color.price

    accessories: List[Accessory] = []
    accessories_price = 0
    accessory_ids = car_create_data.accessory_ids
    for accessory_id in accessory_ids:
        accessory_id = str(accessory_id)
        accessory: Accessory = session.query(Accessory).get(accessory_id)
        if accessory is None:
            raise UnableToFindIdError("Accessory", accessory_id)
        accessories.append(accessory)
        accessories_price += accessory.price

    insurances: List[Insurance] = []
    insurance_price = 0
    insurance_ids = car_create_data.insurance_ids
    for insurance_id in insurance_ids:
        insurance_id = str(insurance_id)
        insurance: Insurance = session.query(Insurance).get(insurance_id)
        if insurance is None:
            raise UnableToFindIdError("Insurance", insurance_id)
        insurances.append(insurance)
        insurance_price += insurance.price

    total_price = model_price + color_price + accessories_price + insurance_price

    customer: Customer = session.query(Customer).get(customer_id)
    if customer is None:
        raise UnableToFindIdError("Customer", customer_id)

    sales_person: SalesPerson = session.query(SalesPerson).get(sales_person_id)
    if sales_person is None:
        raise UnableToFindIdError("Sales Person", sales_person_id)

    car = Car(
        models_id=model.id,
        colors_id=color.id,
        customers_id=customer.id,
        sales_people_id=sales_person.id,
        total_price=total_price,
        purchase_deadline=car_create_data.purchase_deadline,
    )

    for accessory in accessories:
        car.accessories.append(accessory)
    for insurance in insurances:
        car.insurances.append(insurance)

    session.add(car)
    session.commit()
    session.refresh(car)

    return car