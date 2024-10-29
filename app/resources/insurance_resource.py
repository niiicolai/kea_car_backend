from pydantic import BaseModel, ConfigDict, Field, field_validator


class InsuranceBaseResource(BaseModel):
    name: str = Field(..., description="Name of the insurance.", examples=["Flat Tire"])
    price: float = Field(..., description="Price of the insurance.", examples=[9.95])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is None:
            raise ValueError(f"The given insurance name cannot be set to None.")
        value = value.strip()
        if len(value) == 0:
            raise ValueError(f"The given insurance name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is None:
            raise ValueError(f"The given insurance price cannot be set to None.")
        if value < 0:
            raise ValueError(f"The given insurance price {value} cannot be less than zero")
        return value

class InsuranceCreateResource(InsuranceBaseResource):
    pass

class InsuranceUpdateResource(InsuranceBaseResource):
    name: str = Field(None, description="Updated name of the insurance.", examples=["Flat Tire"])
    price: float = Field(None, description="Updated price of the insurance.", examples=[9.95])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class InsuranceReturnResource(InsuranceBaseResource):
    id: str = Field(..., description="The UUID for the insurance.", examples=["8456043d-5fb0-49bf-ac2c-51567a32cc87"])