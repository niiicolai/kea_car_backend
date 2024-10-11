from pydantic import BaseModel, ConfigDict, Field, field_validator
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
    car_id: int = Field(..., examples=[1])

class PurchaseCreateResource(PurchaseCreateOrUpdateResource):
    date_of_purchase: date = Field(default_factory=date.today, examples=[date.today()])


class PurchaseUpdateResource(PurchaseCreateOrUpdateResource):
    car_id: int = Field(None, examples=[1])
    date_of_purchase: date = Field(None, examples=[date.today() - timedelta(days=1)])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)


class PurchaseReturnResource(PurchaseBaseResource):
    id: int = Field(..., examples=[1])
    car: CarReturnResource = Field(...)