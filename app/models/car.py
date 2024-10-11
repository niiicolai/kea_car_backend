from datetime import date
from sqlalchemy import Column, Integer, Double, Date, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.car_resource import CarBaseResource, CarReturnResource
from app.models.model import Model
from app.models.color import Color
from app.models.customer import Customer
from app.models.sales_person import SalesPerson
from app.models.accessory import Accessory, cars_has_accessories


class Car(Base):
    __tablename__ = 'cars'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    models_id: Mapped[int] = Column(Integer, ForeignKey('models.id'), nullable=False)
    colors_id: Mapped[int] = Column(Integer, ForeignKey('colors.id'), nullable=False)
    customers_id: Mapped[int] = Column(Integer, ForeignKey('customers.id'), nullable=False)
    sales_people_id: Mapped[int] = Column(Integer, ForeignKey('sales_people.id'), nullable=False)
    total_price: Mapped[float] = Column(Double, nullable=False)
    purchase_deadline: Mapped[date] = Column(Date, nullable=False)

    purchase = relationship("Purchase", back_populates="car", uselist=False, lazy=False)
    model: Mapped[Model] = relationship("Model", back_populates="cars", lazy=False)
    color: Mapped[Color] = relationship("Color", back_populates="cars", lazy=False)
    customer: Mapped[Customer] = relationship("Customer", back_populates="cars", lazy=False)
    sales_person: Mapped[SalesPerson] = relationship("SalesPerson", back_populates="cars", lazy=False)
    accessories: Mapped[list[Accessory]] = relationship("Accessory", secondary=cars_has_accessories, back_populates="cars", lazy=False)

    def validate_data(self):
        CarBaseResource(
            total_price=self.total_price,
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
        )