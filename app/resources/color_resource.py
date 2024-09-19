from pydantic_core import ValidationError
from pydantic import BaseModel, field_validator
from typing import Optional, Required

class ColorBaseResource(BaseModel):
    color: Optional[str] = None


    class Config:
        from_attributes = True

    @field_validator('color', mode="before")
    def validate_color(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            value = value.strip()
            if value.len(value) == 0:
                raise ValidationError(f"The given color {value} is an empty string.")
        return value

class ColorCreateResource(ColorBaseResource):
    color: str

class ColorUpdateResource(ColorBaseResource):
    pass

class ColorReturnResource(ColorBaseResource):
    id: int

    def to_dict(self) -> dict:
        return {
            'id': self.id
        }
    
    def to_json(self) -> dict:
        as_json = self.to_dict()
        return as_json


