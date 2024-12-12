# External Library imports
from uuid import uuid4
from typing import List, Union, Mapping
from datetime import date
from pymongo.database import Database
from sqlalchemy.orm import Mapped, relationship
from pydantic import BaseModel, ConfigDict, Field, field_validator
from sqlalchemy import Column, String, Double, Date, ForeignKey

# Internal library imports
from db import Base
from app.resources.car_resource import CarReturnResource
from app.models.customer import CustomerMySQLEntity, CustomerMongoEntity
from app.models.sales_person import SalesPersonMySQLEntity, SalesPersonMongoEntity
from app.models.model import (
    ModelMySQLEntity,
    ColorMySQLEntity,
    ModelMongoEntity,
    ColorMongoEntity,
    BrandMongoEntity
)
from app.models.insurance import InsuranceMySQLEntity, InsuranceMongoEntity, cars_has_insurances
from app.models.accessory import AccessoryMySQLEntity, AccessoryMongoEntity, cars_has_accessories


class CarMySQLEntity(Base):
    __tablename__ = 'cars'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    models_id: Mapped[str] = Column(String(36), ForeignKey('models.id'), nullable=False)
    colors_id: Mapped[str] = Column(String(36), ForeignKey('colors.id'), nullable=False)
    customers_id: Mapped[str] = Column(String(36), ForeignKey('customers.id'), nullable=False)
    sales_people_id: Mapped[str] = Column(String(36), ForeignKey('sales_people.id'), nullable=False)
    total_price: Mapped[float] = Column(Double, nullable=False)
    purchase_deadline: Mapped[date] = Column(Date, nullable=False)

    purchase = relationship("PurchaseMySQLEntity", back_populates="car", uselist=False)
    model: Mapped[ModelMySQLEntity] = relationship("ModelMySQLEntity", back_populates="cars", lazy=False)
    color: Mapped[ColorMySQLEntity] = relationship("ColorMySQLEntity", back_populates="cars", lazy=False)
    customer: Mapped[CustomerMySQLEntity] = relationship("CustomerMySQLEntity", back_populates="cars", lazy=False)
    sales_person: Mapped[SalesPersonMySQLEntity] = relationship("SalesPersonMySQLEntity", back_populates="cars",
                                                                lazy=False)
    accessories: Mapped[List[AccessoryMySQLEntity]] = relationship(
        "AccessoryMySQLEntity", secondary=cars_has_accessories, back_populates="cars", lazy=False
    )
    insurances: Mapped[List[InsuranceMySQLEntity]] = relationship(
        "InsuranceMySQLEntity", secondary=cars_has_insurances, back_populates="cars", lazy=False
    )

    car_purchase_view = relationship("CarPurchaseView", back_populates="car", viewonly=True)

    def as_resource(self, is_purchased: bool) -> CarReturnResource:
        if not isinstance(is_purchased, bool):
            raise TypeError(f"is_purchased must be of type bool, "
                            f"not {type(is_purchased).__name__}.")
        return CarReturnResource(
            id=self.id,
            total_price=self.total_price,
            purchase_deadline=self.purchase_deadline,
            model=self.model.as_resource(),
            color=self.color.as_resource(),
            customer=self.customer.as_resource(),
            sales_person=self.sales_person.as_resource(),
            accessories=[accessory.as_resource() for accessory in self.accessories],
            insurances=[insurance.as_resource() for insurance in self.insurances],
            is_purchased=is_purchased,
        )





class CarMongoEntity(BaseModel):  # pragma: no cover
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    total_price: float
    purchase_deadline: Union[date, str]

    model: ModelMongoEntity
    color: ColorMongoEntity
    customer: CustomerMongoEntity
    sales_person: SalesPersonMongoEntity
    accessories: List[AccessoryMongoEntity]
    insurances: List[InsuranceMongoEntity]

    model_config = ConfigDict(from_attributes=True)

    @field_validator("purchase_deadline")
    def validate_purchase_deadline(cls, purchase_deadline: Union[date, str]) -> str:
        if isinstance(purchase_deadline, date):
            return purchase_deadline.isoformat()
        return purchase_deadline

    def as_resource(self, is_purchased: bool) -> CarReturnResource:
        if not isinstance(is_purchased, bool):
            raise TypeError(f"is_purchased must be of type bool, "
                            f"not {type(is_purchased).__name__}.")
        return CarReturnResource(
            id=self.id,
            total_price=self.total_price,
            purchase_deadline=self.purchase_deadline,
            model=self.model.as_resource(),
            color=self.color.as_resource(),
            customer=self.customer.as_resource(),
            sales_person=self.sales_person.as_resource(),
            accessories=[accessory.as_resource() for accessory in self.accessories],
            insurances=[insurance.as_resource() for insurance in self.insurances],
            is_purchased=is_purchased,
        )



def prepare_car_resourcer(database: Database, car: CarReturnResource) -> dict[str, any]:
    model_resource = car.model
    model_brand_resource = model_resource.brand
    model_brand = {
        "_id": model_brand_resource.id,
        "name": model_brand_resource.name,
        "logo_url": model_brand_resource.logo_url,
    }
    model_colors = [
        {
            "_id": color.id,
            "name": color.name,
            "price": color.price,
            "red_value": color.red_value,
            "green_value": color.green_value,
            "blue_value": color.blue_value,
        }
        for color in model_resource.colors
    ]
    model = {
        "_id": model_resource.id,
        "name": model_resource.name,
        "brand": model_brand,
        "colors": model_colors,
        "price": model_resource.price,
        "image_url": model_resource.image_url,
    }
    customer_resource = car.customer
    customer = {
        "_id": customer_resource.id,
        "first_name": customer_resource.first_name,
        "last_name": customer_resource.last_name,
        "email": customer_resource.email,
        "phone_number": customer_resource.phone_number,
        "address": customer_resource.address,
    }
    sales_person_resource = car.sales_person
    sales_person_hashed_password = database.get_collection("sales_people").find_one(
        {"_id": car.sales_person.id}
    ).get("hashed_password")
    if sales_person_hashed_password is None:
        raise Exception("Sales person hashed password not found.")
    sales_person = {
        "_id": sales_person_resource.id,
        "first_name": sales_person_resource.first_name,
        "last_name": sales_person_resource.last_name,
        "email": sales_person_resource.email,
        "hashed_password": sales_person_hashed_password,
    }
    color_resource = car.color
    color = {
        "_id": color_resource.id,
        "name": color_resource.name,
        "price": color_resource.price,
        "red_value": color_resource.red_value,
        "green_value": color_resource.green_value,
        "blue_value": color_resource.blue_value,
    }
    accessories = [
        {
            "_id": accessory.id,
            "name": accessory.name,
            "price": accessory.price,
        }
        for accessory in car.accessories
    ]
    insurances = [
        {
            "_id": insurance.id,
            "name": insurance.name,
            "price": insurance.price,
        }
        for insurance in car.insurances
    ]

    return {
        "_id": car.id,
        "total_price": car.total_price,
        "purchase_deadline": car.purchase_deadline,
        "model": model,
        "color": color,
        "customer": customer,
        "sales_person": sales_person,
        "accessories": accessories,
        "insurances": insurances,
    }


def prepare_car(database: Database, car: Union[Mapping[str, any], dict[str, any], CarReturnResource]) -> CarMongoEntity:
    if isinstance(car, CarReturnResource):
        car = prepare_car_resourcer(database, car)
    print(car.get("customer"))
    customer_entity = CustomerMongoEntity(**car.get("customer"))
    sales_person_entity = SalesPersonMongoEntity(
        **car.get("sales_person")
    )
    model_brand_entity = BrandMongoEntity(**car.get("model").get("brand"))
    model_colors_entities = [ColorMongoEntity(**color) for color in car.get("model").get("colors")]
    car.get("model").pop("brand")
    car.get("model").pop("colors")
    model_entity = ModelMongoEntity(
        **car.get("model"),
        brand=model_brand_entity,
        colors=model_colors_entities
    )
    color_entity = ColorMongoEntity(**car.get("color"))
    accessories_entities = [AccessoryMongoEntity(**accessory) for accessory in car.get("accessories")]
    insurances_entities = [InsuranceMongoEntity(**insurance) for insurance in car.get("insurances")]
    return CarMongoEntity(
        _id=car.get("_id"),
        total_price=car.get("total_price"),
        purchase_deadline=car.get("purchase_deadline"),
        model=model_entity,
        color=color_entity,
        customer=customer_entity,
        sales_person=sales_person_entity,
        accessories=accessories_entities,
        insurances=insurances_entities
    )

