from pydantic import BaseModel, ConfigDict, Field, field_validator, EmailStr

class SalesPersonBaseResource(BaseModel):
    email: EmailStr = Field(..., examples=["tomsemail@gmail.com", "piasemail@gmail.com"])
    first_name: str = Field(..., examples=["Tom", "Pia"])
    last_name: str = Field(..., examples=["Thomsen", "Pil"])
    
    model_config = ConfigDict(from_attributes=True)

    

    
    @field_validator('first_name')
    def validate_first_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given first name {value} is an empty string.")
        return value.strip()
    
    @field_validator('last_name')
    def validate_last_name(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given last name {value} is an empty string.")
        return value.strip()
    

class SalesPersonLoginResource(BaseModel):
    email: EmailStr = Field(..., examples=["tomsemail@gmail.com", "piasemail@gmail.com"])
    password: str = Field(..., examples=["<PASSWORD>", "<PASSWORD>"])

class SalesPersonCreateResource(SalesPersonBaseResource):
    password: str = Field(..., examples=["TomsCode", "PiasCode"])

    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError(f"The given password {value} is an empty string.")
        if ' ' in value:
            raise ValueError(f"The given password {value} contains whitespaces.")
        return value

class SalesPersonUpdateResource(SalesPersonBaseResource):
    email: EmailStr = Field(None, examples=["tomsemail@gmail.com", "piasemail@gmail.com"])
    first_name: str = Field(None, examples=["Tom", "Pia"])
    last_name: str = Field(None, examples=["Thomsen", "Pil"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class SalesPersonReturnResource(SalesPersonBaseResource):
    id: int = Field(..., examples=[1,2])
    