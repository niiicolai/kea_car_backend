from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator

class ColorBaseResource(BaseModel):
    name: str = Field(..., examples=["blue"])
    price: float = Field(..., examples=[99.95])
    red_value: int = Field(..., ge=0, le=255, examples=[0])
    green_value: int = Field(..., ge=0, le=255, examples=[0])
    blue_value: int = Field(..., ge=0, le=255, examples=[255])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given color name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is not None:
            if value < 0:
                raise ValueError(f"The given color price {value} cannot be less than zero")
        return value
    

class ColorCreateResource(ColorBaseResource):
    pass

class ColorUpdateResource(ColorBaseResource):
    name: str = Field(None, examples=["blue"])
    price: float = Field(None, examples=[99.95])
    red_value: int = Field(None, min_length=0, max_length=255, examples=[0])
    green_value: int = Field(None, min_length=0, max_length=255, examples=[0])
    blue_value: int = Field(None, min_length=0, max_length=255, examples=[255])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class ColorReturnResource(ColorBaseResource):
    id: UUID4 = Field(..., examples=["5e755eb3-0099-4cdd-b064-d8bd95968109"])
