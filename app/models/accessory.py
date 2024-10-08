from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import Mapped, relationship
from db import Base
from app.resources.accessory_resource import AccessoryBaseResource, AccessoryReturnResource

class Accessory(Base):
    __tablename__ = 'accessories'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name: Mapped[str] = Column(String(60), unique=True, index=True, nullable=False)
    price: Mapped[float] = Column(Double, nullable=False)
    
    def validate_data(self):
        AccessoryBaseResource(
            name=self.name,
            price=self.price,
        )

    def as_resource(self) -> AccessoryReturnResource:
        return AccessoryReturnResource(
            id=self.id,
            name=self.name,
            price=self.price
        )