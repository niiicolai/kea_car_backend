from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator


class InsuranceBaseResource(BaseModel):
    name: str = Field(..., examples=["Flat Tire"])
    price: float = Field(..., examples=[9.95])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given insurance name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is not None:
            if value < 0:
                raise ValueError(f"The given insurance price {value} cannot be less than zero")
        return value

class InsuranceCreateResource(InsuranceBaseResource):
    pass

class InsuranceUpdateResource(InsuranceBaseResource):
    name: str = Field(None, examples=["Flat Tire"])
    price: float = Field(None, examples=[9.95])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class InsuranceReturnResource(InsuranceBaseResource):
    id: UUID4 = Field(..., examples=["8456043d-5fb0-49bf-ac2c-51567a32cc87"])