from pydantic import BaseModel, ConfigDict, Field, UUID4, field_validator
from typing import Optional

class BrandBaseResource(BaseModel):
    name: str = Field(..., examples=["BMW"])
    logo_url: Optional[str] = Field(..., examples=[None])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given brand name {value} is an empty string.")
        return value

    @field_validator('logo_url')
    def validate_logo_url(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given logo url {value} is an empty string.")
        return value

class BrandCreateResource(BrandBaseResource):
    pass

class BrandUpdateResource(BrandBaseResource):
    name: str = Field(None, examples=["BMW"])
    logo_url: Optional[str] = Field(None, examples=[None])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class BrandReturnResource(BrandBaseResource):
    id: UUID4 = Field(..., examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])