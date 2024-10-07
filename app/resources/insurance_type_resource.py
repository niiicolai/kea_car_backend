from pydantic import BaseModel, ConfigDict, Field, field_validator

class InsuranceTypeBaseResource(BaseModel):
    insurance_name: str = Field(..., examples=["paranormal", "earthquake", "mechanic"])
    price: float = Field(..., examples=[999.95, 69.69, 99.99])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('insurance_name')
    def validate_insurance_name(cls, value: str) -> str:
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

class InsuranceTypeCreateResource(InsuranceTypeBaseResource):
    pass

class InsuranceTypeUpdateResource(InsuranceTypeBaseResource):
    insurance_name: str = Field(None, examples=["paranormal", "earthquake", "mechanic"])
    price: float = Field(None, examples=[999.95, 69.69, 99.99])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class InsuranceTypeReturnResource(InsuranceTypeBaseResource):
    id: int = Field(..., examples=[1,2,3])