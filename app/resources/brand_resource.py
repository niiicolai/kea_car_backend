from pydantic import BaseModel, ConfigDict, Field, field_validator


class BrandBaseResource(BaseModel):
    name: str = Field(..., description="Name of the brand.", examples=["BMW"])
    logo_url: str = Field(..., description="URL from digitaloceanspaces for the brand logo.", examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/bmw-logo.png"])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, name: str) -> str:
        if name is None:
            raise ValueError(f"The given brand name cannot be set to None.")
        name = name.strip()
        if len(name) == 0:
            raise ValueError(f"The given brand name {name} is an empty string.")
        return name

    @field_validator('logo_url')
    def validate_logo_url(cls, logo_url: str) -> str:
        if logo_url is None:
            raise ValueError(f"The given logo url cannot be set to None.")
        logo_url = logo_url.strip()
        if len(logo_url) == 0:
            raise ValueError(f"The given logo url {logo_url} is an empty string.")
        return logo_url

class BrandCreateResource(BrandBaseResource):
    pass

class BrandUpdateResource(BrandBaseResource):
    name: str = Field(None, description="Name of the brand.", examples=["BMW"])
    logo_url: str = Field(None, description="URL from digitaloceanspaces for the brand logo.", examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/bmw-logo.png"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class BrandReturnResource(BrandBaseResource):
    id: str = Field(..., description="UUID of the brand.", examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])