# External Library imports
from typing import List
from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator

# Internal library imports
from app.resources.brand_resource import BrandReturnResource
from app.resources.color_resource import ColorReturnResource


class ModelBaseResource(BaseModel):
    name: str = Field(..., description="Name of the model.", examples=["Series 1"])
    price: float = Field(..., description="Price of the model in kroner.", examples=[10090.95])
    image_url: str = Field(..., description="URL from digitaloceanspaces for the model image.", examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/Series_1.png"])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('name')
    def validate_name(cls, name: str) -> str:
        if name is None:
            raise ValueError("The given model name cannot be None.")
        name = name.strip()
        if len(name) == 0:
            raise ValueError(f"The given model name {name} is an empty string.")
        return name
    
    @field_validator('price')
    def validate_price(cls, price: float) -> float:
        if price is None:
            raise ValueError("The given model price cannot be None.")
        if price < 0:
            raise ValueError(f"The given model price {price} cannot be less than zero")
        return price

    @field_validator('image_url')
    def validate_model_image_url(cls, image_url: str) -> str:
        if image_url is None:
            raise ValueError("The given model image url cannot be None.")
        if len(image_url) == 0:
            raise ValueError(f"The given model image url {image_url} is an empty string.")
        return image_url
    
class ModelCreateOrUpdateResource(ModelBaseResource):
    brands_id: UUID4 = Field(..., description="The UUID of the Brand that the model belongs to.", examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])
    color_ids: List[UUID4] = Field(..., exclude=True, description="The UUIDs of the Colors that the model has.", examples=[["5e755eb3-0099-4cdd-b064-d8bd95968109"],["e2164054-4cb8-49d5-a0da-eca5b36a0b3b"]])
    
    @field_validator('color_ids')
    def validate_color_ids(cls, color_ids: List[UUID4]) -> List[UUID4]:
        if color_ids is None:
            raise ValueError("The given model's colors cannot be None.")
        if color_ids.count == 0:
            raise ValueError("The given model's colors cannot be empty.")
        if len(color_ids) != len(set(color_ids)):
            raise ValueError('color_ids must be unique.')
        return color_ids

class ModelCreateResource(ModelCreateOrUpdateResource):
    pass

class ModelUpdateResource(ModelCreateOrUpdateResource):
    brands_id: UUID4 = Field(None, description="Updated UUID of the Brand that the model belongs to.", examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])
    color_ids: List[UUID4] = Field(default_factory=List[UUID4], exclude=True, description="Updated UUIDs of the Colors that the model has.", examples=[["5e755eb3-0099-4cdd-b064-d8bd95968109"],["e2164054-4cb8-49d5-a0da-eca5b36a0b3b"]])
    name: str = Field(None, description="Updated name of the model.", examples=["Series 1"])
    price: float = Field(None, description="Updated price of the model in kroner.", examples=[10090.95])
    image_url: str = Field(None, description="Updated URL from digitaloceanspaces for the model image.", examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/Series_1.png"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class ModelReturnResource(ModelBaseResource):
    id: str = Field(..., description="The UUID for the model.", examples=["ed996516-a141-4f4e-8991-3edeaba81c14"])
    brand: BrandReturnResource = Field(..., description="The model's Brand as a BrandReturnResource.")
    colors: List[ColorReturnResource] = Field(..., description="The model's Colors as a list of ColorReturnResource.")