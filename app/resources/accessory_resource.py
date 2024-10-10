from pydantic import BaseModel, ConfigDict, Field, field_validator

class AccessoryBaseResource(BaseModel):
    name: str = Field(..., examples=["cup holder","radio", "stereo"])
    price: float = Field(..., examples=[19.99, 99.99, 69.69])
    
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
    name: str = Field(None, examples=["cup holder","radio", "stereo"])
    price: float = Field(None, examples=[19.99, 99.99, 69.69])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class AccessoryReturnResource(AccessoryBaseResource):
    id: int = Field(..., examples=[1,2,3])
