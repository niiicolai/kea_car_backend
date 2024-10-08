from pydantic import BaseModel, ConfigDict, Field, field_validator
from app.resources.brand_resource import BrandReturnResource

class ModelBaseResource(BaseModel):
    model_name: str = Field(..., examples=["iX M60", "F-150 Lightning", "e-tron GT"])
    price: float = Field(..., examples=[9990.95, 690.69, 990.99])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('model_name')
    def validate_model_name(cls, value: str) -> str:
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

class ModelCreateResource(ModelCreateOrUpdateResource):
    pass

class ModelUpdateResource(ModelCreateOrUpdateResource):
    brand_id: int | None = Field(None, examples=[1,2,3])
    model_name: str | None = Field(None, examples=["iX M60", "F-150 Lightning", "e-tron GT"])
    price: float | None = Field(None, examples=[9990.95, 690.69, 990.99])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)
    
class ModelReturnResource(ModelBaseResource):
    id: int = Field(..., examples=[1,2,3])
    brand: BrandReturnResource = Field(..., default_factory=BrandReturnResource)