from pydantic import BaseModel, ConfigDict, Field, field_validator

class AccessoryBaseResource(BaseModel):
    name: str = Field(..., description="Name of the accessory.", examples=["Adaptive Headlights"])
    price: float = Field(..., description="Price of the accessory in kroner.", examples=[99.95])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, name: str) -> str:
        if name is None:
            raise ValueError(f"The given accessory name cannot be set to None.")
        name = name.strip()
        if len(name) == 0:
            raise ValueError(f"The given accessory name {name} is an empty string.")
        return name
    
    @field_validator('price')
    def validate_price(cls, price: float) -> float:
        if price is None:
            raise ValueError(f"The given accessory price cannot be set to None.")
        if price < 0:
            raise ValueError(f"The given accessory price {price} cannot be less than zero")
        return price
    

class AccessoryCreateResource(AccessoryBaseResource):
    pass

class AccessoryUpdateResource(AccessoryBaseResource):
    name: str = Field(None,  description="Name of the accessory.", examples=["Adaptive Headlights"])
    price: float = Field(None, description="Price of the accessory in kroner.", examples=[99.95])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class AccessoryReturnResource(AccessoryBaseResource):
    id: str = Field(..., description="The UUID of the accessory.", examples=["e620ec3c-625d-4bde-9b77-f7449b6352d5"])
