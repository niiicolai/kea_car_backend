# External Library imports
from typing import List
from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator

# Internal library imports
from app.resources.brand_resource import BrandReturnResource
from app.resources.color_resource import ColorReturnResource


class ModelBaseResource(BaseModel):
    name: str = Field(..., examples=["Series 1"])
    price: float = Field(..., examples=[10090.95])
    image_url: str = Field(..., examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/Series_1.png"])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is None:
            raise ValueError("The given model name cannot be None.")
        value = value.strip()
        if len(value) == 0:
            raise ValueError(f"The given model name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is None:
            raise ValueError("The given model price cannot be None.")
        if value < 0:
            raise ValueError(f"The given model price {value} cannot be less than zero")
        return value

    @field_validator('image_url')
    def validate_model_image_url(cls, value: str) -> str:
        if value is None:
            raise ValueError("The given model image url cannot be None.")
        if len(value) == 0:
            raise ValueError(f"The given model image url {value} is an empty string.")
        return value
    
class ModelCreateOrUpdateResource(ModelBaseResource):
    brands_id: UUID4 = Field(..., examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])
    color_ids: List[UUID4] = Field(..., examples=[["5e755eb3-0099-4cdd-b064-d8bd95968109"],["e2164054-4cb8-49d5-a0da-eca5b36a0b3b"]], exclude=True)
    
    @field_validator('color_ids')
    def validate_color_ids(cls, value: List[UUID4]) -> List[UUID4]:
        if value is None:
            raise ValueError("The given model's colors cannot be None.")
        if value.count == 0:
            raise ValueError("The given model's colors cannot be empty.")
        return value

class ModelCreateResource(ModelCreateOrUpdateResource):
    pass

class ModelUpdateResource(ModelCreateOrUpdateResource):
    brands_id: UUID4 = Field(None, examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])
    color_ids: List[UUID4] = Field(default_factory=List[UUID4], examples=[["5e755eb3-0099-4cdd-b064-d8bd95968109"],["e2164054-4cb8-49d5-a0da-eca5b36a0b3b"]], exclude=True)
    name: str = Field(None, examples=["Series 1"])
    price: float = Field(None, examples=[10090.95])
    image_url: str = Field(None, examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/Series_1.png"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class ModelReturnResource(ModelBaseResource):
    id: str = Field(..., examples=["ed996516-a141-4f4e-8991-3edeaba81c14"])
    brand: BrandReturnResource = Field(...)
    colors: List[ColorReturnResource] = Field(...)