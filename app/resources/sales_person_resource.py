from pydantic import BaseModel, ConfigDict, Field, field_validator, EmailStr

class SalesPersonBaseResource(BaseModel):
    email: EmailStr = Field(..., description="Email of the sales person.", examples=["hans@gmail.com"])
    first_name: str = Field(..., description="First name of the sales person.", examples=["Hans"])
    last_name: str = Field(..., description="Last name of the sales person.", examples=["Hansen"])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        if first_name is None:
            raise ValueError(f"The given first name cannot be set to None.")
        first_name = first_name.strip()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        return first_name
    
    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        if last_name is None:
            raise ValueError(f"The given last name cannot be set to None.")
        last_name = last_name.strip()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        return last_name
    

class SalesPersonLoginResource(BaseModel):
    email: EmailStr = Field(..., description="Email of the sales person to login as.", examples=["hans@gmail.com"])
    password: str = Field(..., description="Password of the sales person to login as.", examples=["hans123"])

class SalesPersonCreateResource(SalesPersonBaseResource):
    password: str = Field(..., description="Password of the sales person to create.", examples=["hans123"])

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        if len(password) == 0:
            raise ValueError(f"The given password {password} is an empty string.")
        if ' ' in password:
            raise ValueError(f"The given password {password} contains whitespaces.")
        return password

class SalesPersonUpdateResource(SalesPersonBaseResource):
    email: EmailStr = Field(None, description="Updated email of the sales person.", examples=["hans@gmail.com"])
    first_name: str = Field(None, description="Updated first name of the sales person.", examples=["Hans"])
    last_name: str = Field(None, description="Updated last name of the sales person.", examples=["Hansen"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class SalesPersonReturnResource(SalesPersonBaseResource):
    id: str = Field(..., description="UUID of the sales person.", examples=["f9097a97-eca4-49b6-85a0-08423789c320"])
    