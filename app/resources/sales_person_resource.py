from pydantic import BaseModel, ConfigDict, Field, field_validator, EmailStr

class SalesPersonBaseResource(BaseModel):
    email: EmailStr = Field(..., examples=["hans@gmail.com"])
    first_name: str = Field(..., examples=["Hans"])
    last_name: str = Field(..., examples=["Hansen"])
    
    model_config = ConfigDict(from_attributes=True)


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
    

class SalesPersonLoginResource(BaseModel):
    email: EmailStr = Field(..., examples=["hans@gmail.com"])
    password: str = Field(..., examples=["hans123"])

class SalesPersonCreateResource(SalesPersonBaseResource):
    password: str = Field(..., examples=["hans123"])

    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if len(value) == 0:
            raise ValueError(f"The given password {value} is an empty string.")
        if ' ' in value:
            raise ValueError(f"The given password {value} contains whitespaces.")
        return value

class SalesPersonUpdateResource(SalesPersonBaseResource):
    email: EmailStr = Field(None, examples=["hans@gmail.com"])
    first_name: str = Field(None, examples=["Hans"])
    last_name: str = Field(None, examples=["Hansen"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class SalesPersonReturnResource(SalesPersonBaseResource):
    id: str = Field(..., examples=["f9097a97-eca4-49b6-85a0-08423789c320"])
    