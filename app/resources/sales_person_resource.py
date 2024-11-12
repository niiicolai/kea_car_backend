from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
import re

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


    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        if first_name is None:
            raise ValueError("The given first name cannot be set to None.")
        first_name = first_name.strip()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        """
        # Allow only alphabetic characters, hyphens, and apostrophes
        if not all(c.isalpha() or c in ["-", "'"] for c in first_name):
            raise ValueError("The first name can only contain letters, hyphens, or apostrophes.")
        return str(first_name.capitalize())
        """
        return first_name
    
    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        if last_name is None:
            raise ValueError("The given last name cannot be set to None.")
        last_name = last_name.strip()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        """
        # Allow only alphabetic characters, hyphens, and apostrophes
        if not all(c.isalpha() or c in ["-", "'"] for c in last_name):
            raise ValueError("The last name can only contain letters, hyphens, or apostrophes.")
        return str(last_name.capitalize())
        """
        return last_name
    

class SalesPersonCreateResource(SalesPersonBaseResource):
    password: str = Field(
        default=...,
        description="Password of the sales person to create.", examples=["Hansen123"]
    )

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        if len(password) == 0:
            raise ValueError(f"The given password {password} is an empty string.")
        if ' ' in password:
            raise ValueError(f"The given password {password} contains whitespaces.")
        """
        if len(password) < 8:
            raise ValueError("The given password {password} must be at least 8 characters long.")
        #The password must have at least one uppercase letter, one lower case letter and at least one digit
        if not re.search(r'[A-Z]', password):
            raise ValueError("The password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValueError("The password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValueError("The password must contain at least one digit.")
        """
        return password



class SalesPersonReturnResource(SalesPersonBaseResource):
    id: str = Field(
        default=...,
        description="UUID of the sales person.",
        examples=["f9097a97-eca4-49b6-85a0-08423789c320"]
    )
    