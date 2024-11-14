# External Library imports
from uuid import uuid4
from datetime import date
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, String, Date, ForeignKey

# Internal library imports
from db import Base
from app.models.car import CarMySQLEntity
from app.resources.purchase_resource import PurchaseReturnResource, PurchaseBaseReturnResource


class PurchaseMySQLEntity(Base):
    __tablename__ = 'purchases'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    cars_id: Mapped[str] = Column(String(36), ForeignKey('cars.id'), nullable=False)
    date_of_purchase: Mapped[date] = Column(Date, nullable=False)

    car: Mapped[CarMySQLEntity] = relationship('CarMySQLEntity', back_populates='purchase', uselist=False, lazy=False)

    car_purchase_view = relationship("CarPurchaseView", back_populates="car_purchase", viewonly=True)

    def as_resource_without_car(self) -> PurchaseBaseReturnResource:
        return PurchaseBaseReturnResource(
            id=self.id,
            date_of_purchase=self.date_of_purchase,
        )

    def as_resource(self) -> PurchaseReturnResource:
        return PurchaseReturnResource(
            id=self.id,
            date_of_purchase=self.date_of_purchase,
            car=self.car.as_resource(is_purchased=True),
        )
