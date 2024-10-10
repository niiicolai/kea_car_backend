from pydantic import BaseModel, ConfigDict, Field, field_validator
from app.resources.brand_resource import BrandReturnResource
from app.resources.color_resource import ColorReturnResource

class ModelBaseResource(BaseModel):
    name: str = Field(..., examples=["iX M60", "F-150 Lightning", "e-tron GT"])
    price: float = Field(..., examples=[9990.95, 690.69, 990.99])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given model name {value} is an empty string.")
        return value
    
    @field_validator('price')
    def validate_price(cls, value: float) -> float:
        if value is not None:
            if value < 0:
                raise ValueError(f"The given model price {value} cannot be less than zero")
        return value
    
class ModelCreateOrUpdateResource(ModelBaseResource):
    brand_id: int = Field(..., examples=[1,2,3])
    color_ids: list[int] = Field(..., examples=[[1,2,3],[4,5,6],[7,8,9]], exclude=True)
    
    @field_validator('color_ids')
    def validate_color_ids(cls, value: list[int]) -> list[int]:
        if value is not None:
            if value.count == 0:
                raise ValueError("The given model's colors cannot be zero")
        return value

class ModelCreateResource(ModelCreateOrUpdateResource):
    pass

class ModelUpdateResource(ModelCreateOrUpdateResource):
    brand_id: int = Field(None, examples=[1,2,3])
    color_ids: list[int] = Field(default_factory=list[int], examples=[[1,2,3],[4,5,6],[7,8,9]], exclude=True)
    name: str = Field(None, examples=["iX M60", "F-150 Lightning", "e-tron GT"])
    price: float = Field(None, examples=[9990.95, 690.69, 990.99])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class ModelReturnResource(ModelBaseResource):
    id: int = Field(..., examples=[1,2,3])
    brand: BrandReturnResource = Field(..., default_factory=BrandReturnResource)
    colors: list[ColorReturnResource] = Field(..., default_factory=list[ColorReturnResource])