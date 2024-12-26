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
        minimum_length_of_email = 8
        maximum_length_of_email = 100
        email_length = len(email)
        if email_length < minimum_length_of_email:
            raise ValueError(
                f"The given email {email} is too short, "
                f"it must be at least {minimum_length_of_email} characters long.")
        if email_length > maximum_length_of_email:
            raise ValueError(
                f"The given email {email} is {email_length - maximum_length_of_email} characters too long, "
                f"it can only be maximum {maximum_length_of_email} characters and not {email_length}.")
        return email

    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        minimum_length_of_first_name = 1
        maximum_length_of_first_name = 50
        first_name = first_name.strip()
        if len(first_name) < minimum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too short, "
                             f"it must be at least {minimum_length_of_first_name} characters long.")
        if len(first_name) > maximum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too long, "
                             f"it can only be maximum {maximum_length_of_first_name} characters long.")
        if '  ' in first_name:
            raise ValueError(f"The given first name {first_name} contains extra whitespaces.")
        if not all(part.isalpha() for part in first_name.replace('-', ' ').split()):
            raise ValueError(f"The given first name {first_name} can only contain alphabetic characters.")
        if first_name.startswith('-') or first_name.endswith('-'):
            raise ValueError(f"The given first name {first_name} starts or ends with a hyphen.")
        if ' -' in first_name or '- ' in first_name:
            raise ValueError(f"The given first name {first_name} contains whitespace before or after a hyphen.")
        return first_name.title()

    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        minimum_length_of_last_name = 1
        maximum_length_of_last_name = 50
        last_name = last_name.strip()
        if len(last_name) < minimum_length_of_last_name:
            raise ValueError(f"The given last name {last_name} is too short, "
                             f"it must be at least {minimum_length_of_last_name} characters long.")
        if len(last_name) > maximum_length_of_last_name:
            raise ValueError(f"The given last name {last_name} is too long, "
                             f"it can only be maximum {maximum_length_of_last_name} characters long.")
        if ' ' in last_name:
            raise ValueError(f"The given last name {last_name} contains whitespace.")
        if not all(part.isalpha() for part in last_name.replace('-', ' ').split()):
            raise ValueError(f"The given last name {last_name} can only contain alphabetic characters.")
        if last_name.startswith('-') or last_name.endswith('-'):
            raise ValueError(f"The given last name {last_name} starts or ends with a hyphen.")
        return last_name.title()

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        minimum_length_of_password = 7
        maximum_length_of_password = 30
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
