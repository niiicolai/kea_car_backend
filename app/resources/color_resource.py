from pydantic_core import ValidationError
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Required

class ColorBaseResource(BaseModel):
    color: str = Field(...)
    price: float = Field(...)
    
    def to_dict(self, id: int | None = None) -> dict:
        color_dict = {}
        if id is not None:
            color_dict["id"] = id
        if self.color is not None:
            color_dict["color"] = self.color
        if self.price is not None:
            color_dict["price"] = self.price
        return color_dict


    class Config:
        from_attributes = True

    @field_validator('color')
    def validate_color(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given color {value} is an empty string.")
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
    color: str | None = None
    price: float | None = None

class ColorReturnResource(ColorBaseResource):
    id: int

    def to_json(self) -> dict:
        as_json = self.to_dict(self.id)
        return as_json


