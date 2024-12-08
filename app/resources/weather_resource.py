from pydantic import BaseModel, Field

class WeatherReturnResource(BaseModel):
    temp_c: float = Field(
        default=...,
        description="Temperature in Celsius",
        examples=[-10, 0, 10, 20, 30],
    )