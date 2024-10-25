from pydantic import BaseModel, ConfigDict, Field, UUID4
from datetime import date
from app.resources.car_resource import CarReturnResource


class PurchaseBaseResource(BaseModel):

    model_config = ConfigDict(from_attributes=True)

class PurchaseCreateResource(PurchaseBaseResource):
    cars_id: UUID4 = Field(..., examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])


class PurchaseReturnResource(PurchaseBaseResource):
    id: str = Field(..., examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])
    date_of_purchase: date = Field(..., examples=[date.today()])
    car: CarReturnResource = Field(...)