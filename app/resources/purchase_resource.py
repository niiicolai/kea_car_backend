from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import date, timedelta


class PurchaseBaseResource(BaseModel):
    date_of_purchase: date = Field(..., examples=[date.today()])

    model_config = ConfigDict(from_attributes=True)

    @field_validator('date_of_purchase')
    def validate_date_of_purchase(cls, value: date) -> date:
        if value is None:
            raise ValueError(f"The given date of purchase must not be None.")
        return value


class PurchaseCreateResource(PurchaseBaseResource):
    date_of_purchase: date = Field(default_factory=date.today, examples=[date.today()])


class PurchaseUpdateResource(PurchaseBaseResource):
    date_of_purchase: date = Field(None, examples=[date.today() - timedelta(days=1)])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)


class PurchaseReturnResource(PurchaseBaseResource):
    id: int = Field(..., examples=[1, 2, 3])