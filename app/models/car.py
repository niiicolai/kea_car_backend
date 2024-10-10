from datetime import date
from sqlalchemy import Column, Integer, Double, Date, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.car_resource import CarBaseResource, CarReturnResource
from app.models.model import Model


class Car(Base):
    __tablename__ = 'cars'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    models_id: Mapped[int] = Column(Integer, ForeignKey('models.id'), nullable=False)
    total_price: Mapped[float] = Column(Double, nullable=False)
    purchase_deadline: Mapped[date] = Column(Date, nullable=False)

    purchase = relationship("Purchase", back_populates="car", uselist=False, lazy=False)
    model: Mapped[Model] = relationship("Model", back_populates="cars", lazy=False)

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
        )