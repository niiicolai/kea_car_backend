from pydantic import BaseModel, ConfigDict, Field, field_validator

class ColorBaseResource(BaseModel):
    name: str = Field(..., examples=["black","white", "grey"])
    price: float = Field(..., examples=[0.0, 99.99, 69.69])
    red_value: int = Field(..., min_length=0, max_length=255, examples=[0, 255, 128])
    green_value: int = Field(..., min_length=0, max_length=255, examples=[0, 255, 128])
    blue_value: int = Field(..., min_length=0, max_length=255, examples=[0, 255, 128])
    
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
    name: str = Field(None, examples=["black","white", "grey"])
    price: float = Field(None, examples=[0.0, 99.99, 69.69])
    red_value: int = Field(None, min_length=0, max_length=255, examples=[0, 255, 128])
    green_value: int = Field(None, min_length=0, max_length=255, examples=[0, 255, 128])
    blue_value: int = Field(None, min_length=0, max_length=255, examples=[0, 255, 128])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class ColorReturnResource(ColorBaseResource):
    id: int = Field(..., examples=[1,2,3])
