# External Library imports
from typing import Optional
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, String, ForeignKey, Boolean

# Internal library imports
from db import Base
from app.models.customer import CustomerMySQLEntity
from app.models.sales_person import SalesPersonMySQLEntity
from app.models.purchase import PurchaseMySQLEntity, CarMySQLEntity
from app.resources.view_resources.car_purchase_resource import (
    CarPurchaseCustomerReturnResource,
    CarPurchaseSalePersonReturnResource,
    CarPurchaseReturnResource
)


class CarPurchaseView(Base):
    __tablename__ = 'car_purchase_view'
    car_id: Mapped[str] = Column(String(36), ForeignKey('cars.id'), primary_key=True, index=True, nullable=False)
    purchase_id: Mapped[Optional[str]] = Column(String(36), ForeignKey('purchases.id'), nullable=True)
    customer_id: Mapped[str] = Column(String(36), ForeignKey('customers.id'), nullable=False)
    sales_person_id: Mapped[str] = Column(String(36), ForeignKey('sales_people.id'), nullable=False)
    is_past_deadline: Mapped[bool] = Column(Boolean, nullable=False)

    car: Mapped[CarMySQLEntity] = relationship("CarMySQLEntity", back_populates="car_purchase_view", lazy=False)
    car_purchase: Mapped[Optional[PurchaseMySQLEntity]] = relationship("PurchaseMySQLEntity", back_populates="car_purchase_view", lazy=False)
    car_customer: Mapped[CustomerMySQLEntity] = relationship("CustomerMySQLEntity", back_populates="car_purchase_view", lazy=False)
    car_sales_person: Mapped[SalesPersonMySQLEntity] = relationship("SalesPersonMySQLEntity", back_populates="car_purchase_view", lazy=False)

    def as_customer_resource(self) -> CarPurchaseCustomerReturnResource:
        return CarPurchaseCustomerReturnResource(
            id=self.car_id,
            total_price=self.car.total_price,
            purchase_deadline=self.car.purchase_deadline,
            is_past_deadline=self.is_past_deadline,
            model=self.car.model.as_resource_without_colors(),
            color=self.car.color.as_resource(),
            purchase=self.car_purchase.as_resource_without_car() if self.car_purchase else None,
            sales_person=self.car_sales_person.as_resource(),
            accessories=[accessory.as_resource() for accessory in self.car.accessories],
            insurances=[insurance.as_resource() for insurance in self.car.insurances],
        )

    def as_sales_person_resource(self) -> CarPurchaseSalePersonReturnResource:
        return CarPurchaseSalePersonReturnResource(
            id=self.car_id,
            total_price=self.car.total_price,
            purchase_deadline=self.car.purchase_deadline,
            is_past_deadline=self.is_past_deadline,
            model=self.car.model.as_resource_without_colors(),
            color=self.car.color.as_resource(),
            purchase=self.car_purchase.as_resource_without_car() if self.car_purchase else None,
            customer=self.car_customer.as_resource(),
            accessories=[accessory.as_resource() for accessory in self.car.accessories],
            insurances=[insurance.as_resource() for insurance in self.car.insurances],
        )

    def as_resource(self) -> CarPurchaseReturnResource:
        return CarPurchaseReturnResource(
            id=self.car_id,
            total_price=self.car.total_price,
            purchase_deadline=self.car.purchase_deadline,
            is_past_deadline=self.is_past_deadline,
            model=self.car.model.as_resource_without_colors(),
            color=self.car.color.as_resource(),
            purchase=self.car_purchase.as_resource_without_car() if self.car_purchase else None,
            sales_person=self.car_sales_person.as_resource(),
            customer=self.car_customer.as_resource(),
            accessories=[accessory.as_resource() for accessory in self.car.accessories],
            insurances=[insurance.as_resource() for insurance in self.car.insurances],
        )
