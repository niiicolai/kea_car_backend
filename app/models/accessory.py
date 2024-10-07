from sqlalchemy import Column, Integer, String, Double
from db import Base
from app.resources.accessory_resource import AccessoryBaseResource, AccessoryReturnResource

class Accessory(Base):
    __tablename__ = 'accessories'
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    accessory_name: str = Column(String(60), unique=True, index=True, nullable=False)
    price: float = Column(Double, nullable=False)
    
    def validate_data(self):
        AccessoryBaseResource(
            accessory_name=self.accessory_name,
            price=self.price,
        )

    def as_resource(self) -> AccessoryReturnResource:
        return AccessoryReturnResource(
            id=self.id,
            accessory_name=self.accessory_name,
            price=self.price
        )