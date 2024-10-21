from datetime import date
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.purchase_resource import PurchaseBaseResource, PurchaseReturnResource
from app.models.car import Car
from uuid import uuid4


class Purchase(Base):
    __tablename__ = 'purchases'
    id: Mapped[str] = Column(String(36), primary_key=True, default=lambda: str(uuid4()), index=True, nullable=False)
    cars_id: Mapped[str] = Column(String(36), ForeignKey('cars.id'), nullable=False)
    date_of_purchase: Mapped[date] = Column(Date, nullable=False)

    car: Mapped[Car] = relationship('Car', back_populates='purchase', uselist=False, lazy=False)

    def validate_data(self):
        PurchaseBaseResource(
            date_of_purchase=self.date_of_purchase,
        )

    def as_resource(self) -> PurchaseReturnResource:
        return PurchaseReturnResource(
            id=self.id,
            date_of_purchase=self.date_of_purchase,
            car=self.car,
        )