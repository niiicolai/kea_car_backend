from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

class SalesPersonLoginResource(BaseModel):
    email: EmailStr = Field(
        default=...,
        description="Email of the sales person to login as.",
        examples=["hans@gmail.com"]
    )
    password: str = Field(
        default=...,
        description="Password of the sales person to login as.",
        examples=["hans123"]
    )

class SalesPersonBaseResource(BaseModel):
    email: EmailStr = Field(
        default=...,
        description="Email of the sales person.",
        examples=["hans@gmail.com"]
    )
    first_name: str = Field(
        default=...,
        description="First name of the sales person.",
        examples=["Hans"]
    )
    last_name: str = Field(
        default=...,
        description="Last name of the sales person.",
        examples=["Hansen"]
    )
    
    model_config = ConfigDict(from_attributes=True)



class SalesPersonCreateResource(SalesPersonBaseResource):
    password: str = Field(
        default=...,
        description="Password of the sales person to create.", examples=["Hansen123"]
    )

    @field_validator('email')
    def validate_email(cls, email: str) -> str:
        maximum_length_of_email = 100
        email_length = len(email)
        if email_length > maximum_length_of_email:
            raise ValueError(
                f"The given email {email} is {email_length - maximum_length_of_email} characters too long, "
                f"it can only be maximum {maximum_length_of_email} characters and not {email_length}.")
        return email

    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        first_name = first_name.strip()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        return first_name

    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        last_name = last_name.strip()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        return last_name

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        if len(password) == 0:
            raise ValueError(f"The given password {password} is an empty string.")
        if ' ' in password:
            raise ValueError(f"The given password {password} contains whitespaces.")
        return password



class SalesPersonReturnResource(SalesPersonBaseResource):
    id: str = Field(
        default=...,
        description="UUID of the sales person.",
        examples=["f9097a97-eca4-49b6-85a0-08423789c320"]
    )
    