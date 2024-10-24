from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator
from datetime import date, timedelta
from app.resources.car_resource import CarReturnResource


class PurchaseBaseResource(BaseModel):
    date_of_purchase: date = Field(..., examples=[date.today()])

    model_config = ConfigDict(from_attributes=True)

    @field_validator('date_of_purchase')
    def validate_date_of_purchase(cls, value: date) -> date:
        if value is None:
            raise ValueError(f"The given date of purchase must not be None.")
        return value

class PurchaseCreateOrUpdateResource(PurchaseBaseResource):
    car_id: UUID4 = Field(..., examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])

class PurchaseCreateResource(PurchaseCreateOrUpdateResource):
    date_of_purchase: date = Field(default_factory=date.today, examples=[date.today()])


class PurchaseUpdateResource(PurchaseCreateOrUpdateResource):
    car_id: UUID4 = Field(None, examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])
    date_of_purchase: date = Field(None, examples=[date.today() - timedelta(days=1)])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)


class PurchaseReturnResource(PurchaseBaseResource):
    id: str = Field(..., examples=["6b00d785-bdb8-4441-9590-04938eefa481"])
    car: CarReturnResource = Field(...)