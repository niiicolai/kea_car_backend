from pydantic import BaseModel, ConfigDict, Field, field_validator

class ColorBaseResource(BaseModel):
    name: str = Field(
        default=...,
        description="Name of the color.",
        examples=["blue"]
    )
    price: float = Field(
        default=...,
        description="Price of the color in kroner.",
        examples=[99.95]
    )
    red_value: int = Field(
        default=...,
        ge=0, le=255,
        description="The red RGB value for the color.",
        examples=[0]
    )
    green_value: int = Field(
        default=...,
        ge=0, le=255,
        description="The green RGB value for the color.", examples=[0]
    )
    blue_value: int = Field(
        default=...,
        ge=0, le=255,
        description="The blue RGB value for the color.",
        examples=[255]
    )
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def validate_name(cls, name: str) -> str:
        if name is None:
            raise ValueError("The given color name cannot be set to None.")
        name = name.strip()
        if len(name) == 0:
            raise ValueError(f"The given color name {name} is an empty string.")
        return name
    
    @field_validator('price')
    def validate_price(cls, price: float) -> float:
        if price is None:
            raise ValueError("The given color price cannot be set to None.")
        if price < 0:
            raise ValueError(f"The given color price {price} cannot be less than zero")
        return price

    @field_validator('red_value')
    def validate_red_value(cls, red_value: int) -> int:
        if red_value is None:
            raise ValueError("The given color's red RGB value cannot be set to None.")
        return red_value

    @field_validator('green_value')
    def validate_green_value(cls, green_value: int) -> int:
        if green_value is None:
            raise ValueError("The given color's green RGB value cannot be set to None.")
        return green_value

    @field_validator('blue_value')
    def validate_blue_value(cls, blue_value: int) -> int:
        if blue_value is None:
            raise ValueError("The given color's blue RGB value cannot be set to None.")
        return blue_value


class ColorReturnResource(ColorBaseResource):
    id: str = Field(
        default=...,
        description="The UUID for the color.",
        examples=["5e755eb3-0099-4cdd-b064-d8bd95968109"]
    )
