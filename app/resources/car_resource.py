from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import date, timedelta

def calculate_purchase_deadline() -> date:
    return date.today() + timedelta(days=30)

class CarBaseResource(BaseModel):
    total_price: float = Field(..., gt=0, examples=[999.99])
    purchase_deadline: date = Field(..., examples=[calculate_purchase_deadline()])

    model_config = ConfigDict(from_attributes=True)

    @field_validator('total_price')
    def validate_total_price(cls, value: float) -> float:
        if value < 0:
            raise ValueError('total price must be positive')
        return value

    @field_validator('purchase_deadline')
    def validate_purchase_deadline(cls, value: date) -> date:
        if value is None:
            raise ValueError(f"The given purchase deadline must not be None.")
        return value


class CarCreateResource(CarBaseResource):
    purchase_deadline: date = Field(default_factory=calculate_purchase_deadline, examples=[calculate_purchase_deadline()])


class CarUpdateResource(CarBaseResource):
    total_price: float = Field(None, gt=0, examples=[999.99])
    date_of_purchase: date = Field(None, examples=[calculate_purchase_deadline()])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)


class CarReturnResource(CarBaseResource):
    id: int = Field(..., examples=[1])