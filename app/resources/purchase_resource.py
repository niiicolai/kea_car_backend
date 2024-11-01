# External Library imports
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, UUID4

# Internal library imports
from app.resources.car_resource import CarReturnResource


class PurchaseBaseResource(BaseModel):

    model_config = ConfigDict(from_attributes=True)

class PurchaseCreateResource(PurchaseBaseResource):
    date_of_purchase: date = Field(default_factory=date.today, description="The date of the purchase for when the purchase was made.", examples=[date.today()])
    cars_id: UUID4 = Field(..., description="UUID of the Car that the purchase belongs to.", examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])


class PurchaseReturnResource(PurchaseBaseResource):
    id: str = Field(..., description="UUID of the purchase.", examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])
    date_of_purchase: date = Field(..., description="The date of the purchase for when the purchase was made.", examples=[date.today()])
    car: CarReturnResource = Field(..., description="The purchase's Car as a CarReturnResource.")