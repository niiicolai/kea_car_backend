from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator
from datetime import date, timedelta
from app.resources.model_resource import ModelReturnResource, ColorReturnResource
from app.resources.customer_resource import CustomerReturnResource
from app.resources.sales_person_resource import SalesPersonReturnResource
from app.resources.accessory_resource import AccessoryReturnResource
from app.resources.insurance_resource import InsuranceReturnResource
from typing import List

def calculate_purchase_deadline() -> date:
    return date.today() + timedelta(days=30)

class CarBaseResource(BaseModel):
    purchase_deadline: date = Field(..., examples=[calculate_purchase_deadline()])

    model_config = ConfigDict(from_attributes=True)

    @field_validator('purchase_deadline')
    def validate_purchase_deadline(cls, value: date) -> date:
        if value is None:
            raise ValueError(f"The given purchase deadline must not be None.")
        return value

class CarCreateOrUpdateResource(CarBaseResource):
    models_id: UUID4 = Field(..., examples=["ed996516-a141-4f4e-8991-3edeaba81c14"])
    colors_id: UUID4 = Field(..., examples=["5e755eb3-0099-4cdd-b064-d8bd95968109"])
    customers_id: UUID4 = Field(..., examples=["0ac1d668-55aa-46a1-898a-8fa61457facb"])
    sales_people_id: UUID4 = Field(..., examples=["f9097a97-eca4-49b6-85a0-08423789c320"])
    accessory_ids: List[UUID4] = Field(default_factory=list[UUID4], exclude=True, examples=[["e620ec3c-625d-4bde-9b77-f7449b6352d5","fc8f689e-9615-4cf6-9664-31400db7ebea"]])
    insurance_ids: List[UUID4] = Field(default_factory=list[UUID4], exclude=True, examples=[["8456043d-5fb0-49bf-ac2c-51567a32cc87","76b21d38-2103-4464-84f2-c87178e4a30c"]])

    @field_validator('accessory_ids')
    def validate_accessory_ids(cls, accessory_ids: List[UUID4]) -> List[UUID4]:
        if len(accessory_ids) != len(set(accessory_ids)):
            raise ValueError('accessory_ids must be unique')
        return accessory_ids

    @field_validator('insurance_ids')
    def validate_insurance_ids(cls, insurance_ids: List[UUID4]) -> List[UUID4]:
        if len(insurance_ids) != len(set(insurance_ids)):
            raise ValueError('insurance_ids must be unique')
        return insurance_ids


class CarCreateResource(CarCreateOrUpdateResource):
    purchase_deadline: date = Field(default_factory=calculate_purchase_deadline, examples=[calculate_purchase_deadline()])


class CarUpdateResource(CarCreateOrUpdateResource):
    models_id: UUID4 = Field(None, examples=["ed996516-a141-4f4e-8991-3edeaba81c14"])
    colors_id: UUID4 = Field(None, examples=["5e755eb3-0099-4cdd-b064-d8bd95968109"])
    customers_id: UUID4 = Field(None, examples=["0ac1d668-55aa-46a1-898a-8fa61457facb"])
    sales_people_id: UUID4 = Field(None, examples=["f9097a97-eca4-49b6-85a0-08423789c320"])
    total_price: float = Field(None, gt=0, examples=[999.99])
    purchase_deadline: date = Field(None, examples=[calculate_purchase_deadline()])

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class CarReturnResource(CarBaseResource):
    total_price: float = Field(..., gt=0, examples=[999.99])
    id: str = Field(..., examples=["e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a"])
    model: ModelReturnResource = Field(...)
    color: ColorReturnResource = Field(...)
    customer: CustomerReturnResource = Field(...)
    sales_person: SalesPersonReturnResource = Field(...)
    accessories: List[AccessoryReturnResource] = Field(...)
    insurances: List[InsuranceReturnResource] = Field(...)
