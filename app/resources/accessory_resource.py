from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator

class AccessoryBaseResource(BaseModel):
    name: str = Field(..., examples=["Adaptive Headlights"])
    price: float = Field(..., examples=[99.95])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given accessory name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is not None:
            if value < 0:
                raise ValueError(f"The given accessory price {value} cannot be less than zero")
        return value
    

class AccessoryCreateResource(AccessoryBaseResource):
    pass

class AccessoryUpdateResource(AccessoryBaseResource):
    name: str = Field(None, examples=["Adaptive Headlights"])
    price: float = Field(None, examples=[99.95])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class AccessoryReturnResource(AccessoryBaseResource):
    id: str = Field(..., examples=["e620ec3c-625d-4bde-9b77-f7449b6352d5"])
