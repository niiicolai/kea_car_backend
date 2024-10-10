from pydantic import BaseModel, ConfigDict, Field, field_validator

class SalesPersonBaseResource(BaseModel):
    email: str = Field(..., examples=["tomsemail@gmail.com", "piasemail@gmail.com"])
    password: str = Field(..., examples=["TomsCode", "PiasCode"])
    first_name: str = Field(..., examples=["Tom", "Pia"])
    last_name: str = Field(..., examples=["Thomsen", "Pil"])
    
    model_config = ConfigDict(from_attributes=True)
    
    @field_validator('email')
    def validate_email(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given email {value} is an empty string.")
        return value
    
    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given password {value} is an empty string.")
        return value
    
    @field_validator('first_name')
    def validate_first_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given first name {value} is an empty string.")
        return value
    
    @field_validator('last_name')
    def validate_last_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given last name {value} is an empty string.")
        return value
    

class SalesPersonCreateResource(SalesPersonBaseResource):
    pass

class SalesPersonUpdateResource(SalesPersonBaseResource):
    email: str = Field(None, examples=["tomsemail@gmail.com", "piasemail@gmail.com"])
    password: str = Field(None, examples=["TomsCode", "PiasCode"])
    first_name: str = Field(None, examples=["Tom", "Pia"])
    last_name: str = Field(None, examples=["Thomsen", "Pil"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class SalesPersonReturnResource(SalesPersonBaseResource):
    id: int = Field(..., examples=[1,2])
    