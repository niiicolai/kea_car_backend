from pydantic import BaseModel, ConfigDict, Field, field_validator
from datetime import date, timedelta
from app.resources.model_resource import ModelReturnResource, ColorReturnResource
from app.resources.customer_resource import CustomerReturnResource

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

class CarCreateOrUpdateResource(CarBaseResource):
    models_id: int = Field(..., examples=[1])
    colors_id: int = Field(..., examples=[1])


class CarCreateResource(CarCreateOrUpdateResource):
    purchase_deadline: date = Field(default_factory=calculate_purchase_deadline, examples=[calculate_purchase_deadline()])


class CarUpdateResource(CarCreateOrUpdateResource):
    models_id: int = Field(None, gt=0, examples=[1])
    colors_id: int = Field(None, exclude=True, examples=[1])
    total_price: float = Field(None, gt=0, examples=[999.99])
    purchase_deadline: date = Field(None, examples=[calculate_purchase_deadline()])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)


class CarReturnResource(CarBaseResource):
    id: int = Field(..., examples=[1])
    model: ModelReturnResource = Field(..., default_factory=ModelReturnResource)
    color: ColorReturnResource = Field(..., default_factory=ColorReturnResource)
    customer: CustomerReturnResource = Field(..., default_factory=CustomerReturnResource)
