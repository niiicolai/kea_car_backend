# External Library imports
from uuid import uuid4
from typing import List
from datetime import date
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, String, Double, Date, ForeignKey

# Internal library imports
from db import Base
from app.models.model import Model
from app.models.color import Color
from app.models.customer import Customer
from app.models.sales_person import SalesPerson
from app.models.insurance import Insurance, cars_has_insurances
from app.models.accessory import Accessory, cars_has_accessories
from app.resources.car_resource import CarBaseResource, CarReturnResource


class Car(Base):
    __tablename__ = 'cars'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    models_id: Mapped[str] = Column(String(36), ForeignKey('models.id'), nullable=False)
    colors_id: Mapped[str] = Column(String(36), ForeignKey('colors.id'), nullable=False)
    customers_id: Mapped[str] = Column(String(36), ForeignKey('customers.id'), nullable=False)
    sales_people_id: Mapped[str] = Column(String(36), ForeignKey('sales_people.id'), nullable=False)
    total_price: Mapped[float] = Column(Double, nullable=False)
    purchase_deadline: Mapped[date] = Column(Date, nullable=False)

    purchase = relationship("Purchase", back_populates="car", uselist=False)
    model: Mapped[Model] = relationship("Model", back_populates="cars", lazy=False)
    color: Mapped[Color] = relationship("Color", back_populates="cars", lazy=False)
    customer: Mapped[Customer] = relationship("Customer", back_populates="cars", lazy=False)
    sales_person: Mapped[SalesPerson] = relationship("SalesPerson", back_populates="cars", lazy=False)
    accessories: Mapped[List[Accessory]] = relationship("Accessory", secondary=cars_has_accessories, back_populates="cars", lazy=False)
    insurances: Mapped[List[Insurance]] = relationship("Insurance", secondary=cars_has_insurances, back_populates="cars", lazy=False)

    def validate_data(self):
        CarBaseResource(
            purchase_deadline=self.purchase_deadline,
        )

    def as_resource(self) -> CarReturnResource:
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
        )