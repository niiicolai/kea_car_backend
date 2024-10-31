from pydantic import BaseModel, ConfigDict, Field


class BrandBaseResource(BaseModel):
    name: str = Field(..., description="Name of the brand.", examples=["BMW"])
    logo_url: str = Field(..., description="URL from digitaloceanspaces for the brand logo.", examples=["https://keacar.ams3.cdn.digitaloceanspaces.com/bmw-logo.png"])
    
    model_config = ConfigDict(from_attributes=True)


class BrandReturnResource(BrandBaseResource):
    id: str = Field(..., description="UUID of the brand.", examples=["feb2efdb-93ee-4f45-88b1-5e4086c00334"])