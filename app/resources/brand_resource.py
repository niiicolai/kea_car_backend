from pydantic import BaseModel, ConfigDict, Field, field_validator

class BrandBaseResource(BaseModel):
    brand_name: str = Field(..., examples=["BMW","Ford", "Audi"])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('brand_name')
    def validate_color(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given brand name {value} is an empty string.")
        return value
    

class BrandCreateResource(BrandBaseResource):
    pass

class BrandUpdateResource(BrandBaseResource):
    Brand_name: str | None = Field(None, examples=["BMW","Ford", "Audi"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class BrandReturnResource(BrandBaseResource):
    id: int = Field(..., examples=[1,2,3])