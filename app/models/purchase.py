from datetime import date
from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.purchase_resource import PurchaseBaseResource, PurchaseReturnResource


class Purchase(Base):
    __tablename__ = 'purchases'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    date_of_purchase: Mapped[date] = Column(Date, nullable=False)

    def validate_data(self):
        PurchaseBaseResource(
            date_of_purchase=self.date_of_purchase,
        )

    def as_resource(self) -> PurchaseReturnResource:
        return PurchaseReturnResource(
            id=self.id,
            date_of_purchase=self.date_of_purchase,
        )