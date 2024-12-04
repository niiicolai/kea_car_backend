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
        minimum_length_of_first_name = 2
        maximum_length_of_first_name = 50
        first_name = first_name.strip().capitalize()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        if len(first_name) < minimum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too short, "
                             f"it must be at least {minimum_length_of_first_name} characters long.")
        if len(first_name) > maximum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too long, "
                             f"it can only be maximum {maximum_length_of_first_name} characters long.")
        if ' ' in first_name:
            raise ValueError(f"The given first name {first_name} contains whitespace.")
        if not first_name.isalpha():
            raise ValueError(f"The given first name {first_name} can only contain alphabetic characters.")
        return first_name

    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        minimum_length_of_last_name = 2
        maximum_length_of_last_name = 50
        last_name = last_name.strip().capitalize()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        if len(last_name) < minimum_length_of_last_name:
            raise ValueError(f"The given last name {last_name} is too short, "
                             f"it must be at least {minimum_length_of_last_name} characters long.")
        if len(last_name) > maximum_length_of_last_name:
            raise ValueError(f"The given last name {last_name} is too long, "
                             f"it can only be maximum {maximum_length_of_last_name} characters long.")
        if ' ' in last_name:
            raise ValueError(f"The given last name {last_name} contains whitespace.")
        if not last_name.isalpha():
            raise ValueError(f"The given last name {last_name} can only contain alphabetic characters.")
        return last_name

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        minimum_length_of_password = 7
        maximum_length_of_password = 30
        if len(password) == 0:
            raise ValueError(f"The given password {password} is an empty string.")
        if ' ' in password:
            raise ValueError(f"The given password {password} contains whitespaces.")
        if len(password) > maximum_length_of_password:
            raise ValueError(f"The given password {password} is too long, "
                             f"it can only be maximum {maximum_length_of_password} characters long.")
        if len(password) < minimum_length_of_password:
            raise ValueError(f"The given password {password} is too short, "
                             f"it must be at least {minimum_length_of_password} characters long.")
        return password



class SalesPersonReturnResource(SalesPersonBaseResource):
    id: str = Field(
        default=...,
        description="UUID of the sales person.",
        examples=["f9097a97-eca4-49b6-85a0-08423789c320"]
    )
    