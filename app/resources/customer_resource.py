from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, ValidationInfo, field_validator


class CustomerBaseResource(BaseModel):
    email: EmailStr = Field(
        default=...,
        description="Email of the customer.",
        examples=["henrik@gmail.com"]
    )
    phone_number: Optional[str] = Field(
        default=...,
        description="Phone number of the customer.",
        examples=["10203040"]
    )
    first_name: str = Field(
        default=...,
        description="First name of the customer.",
        examples=["'Henrik"]
    )
    last_name: str = Field(
        default=...,
        description="Last name of the customer.",
        examples=["Henriksen"]
    )
    address: Optional[str] = Field(
        default=...,
        description="Address of the customer.",
        examples=["Randomgade nr. 10 4. tv."]
    )
    
    model_config = ConfigDict(from_attributes=True)

    @field_validator('email')
    def validate_email(cls, email: str) -> str:
        maximum_length_of_email = 100
        if email is None:
            raise ValueError("The given email cannot be set to None.")
        email_length = len(email)
        if email_length > maximum_length_of_email:
            raise ValueError(f"The given email {email} is {email_length - maximum_length_of_email} characters too long, "
                             f"it can only be maximum {maximum_length_of_email} characters and not {email_length}.")
        return email

    @field_validator('phone_number')
    def validate_phone_number(cls, phone_number: Optional[str]) -> Optional[str]:
        minimum_length_of_phone_number = 8
        maximum_length_of_phone_number = 30
        if phone_number is not None:
            phone_number = phone_number.strip()
            if len(phone_number) == 0:
                raise ValueError(f"The given phone number {phone_number} is an empty string.")
            if len(phone_number) < minimum_length_of_phone_number:
                raise ValueError(f"The given phone number {phone_number} is too short, "
                                 f"it must be at least {minimum_length_of_phone_number} characters long.")
            if len(phone_number) > maximum_length_of_phone_number:
                raise ValueError(f"The given phone number {phone_number} is too long, "
                                 f"it can only be maximum {maximum_length_of_phone_number} characters long.")
            if phone_number.startswith('+'):
                if not phone_number[1:].isdigit():
                    raise ValueError(f"The given phone number {phone_number} can only contain digits after the '+'.")
            elif not phone_number.isdigit():
                raise ValueError(f"The given phone number {phone_number} can only contain digits.")
        return phone_number
    
    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        minimum_length_of_first_name = 2
        maximum_length_of_first_name = 45
        if first_name is None:
            raise ValueError("The given first name cannot be set to None.")
        first_name = first_name.strip().capitalize()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        if len(first_name) < minimum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too short, "
                             f"it must be at least {minimum_length_of_first_name} characters long.")
        if len(first_name) > maximum_length_of_first_name:
            raise ValueError(f"The given first name {first_name} is too long, "
                             f"it can only be maximum {maximum_length_of_first_name} characters long.")
        if not first_name.isalpha():
            raise ValueError(f"The given first name {first_name} can only contain alphabetic characters.")
        return first_name
    
    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        minimum_length_of_first_name = 2
        maximum_length_of_first_name = 45
        if last_name is None:
            raise ValueError("The given last name cannot be set to None.")
        last_name = last_name.strip().capitalize()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        if len(last_name) < minimum_length_of_first_name:
            raise ValueError(f"The given last name {last_name} is too short, "
                             f"it must be at least {minimum_length_of_first_name} characters long.")
        if len(last_name) > maximum_length_of_first_name:
            raise ValueError(f"The given last name {last_name} is too long, "
                             f"it can only be maximum {maximum_length_of_first_name} characters long.")
        if not last_name.isalpha():
            raise ValueError(f"The given last name {last_name} can only contain alphabetic characters.")
        return last_name
    
    @field_validator('address')
    def validate_address(cls, address: Optional[str]) -> Optional[str]:
        minimum_length_of_address = 5
        maximum_length_of_address = 255
        if address is not None:
            address = address.strip()
            if len(address) == 0:
                raise ValueError(f"The given address {address} is an empty string.")
            if len(address) < minimum_length_of_address:
                raise ValueError(f"The given address {address} is too short, "
                                 f"it must be at least {minimum_length_of_address} characters long.")
            if len(address) > maximum_length_of_address:
                raise ValueError(f"The given address {address} is too long, "
                                 f"it can only be maximum {maximum_length_of_address} characters long.")
            if '  ' in address:
                raise ValueError(f"The given address {address} contains multiple whitespaces.")
        return address

    @field_validator('*', mode='before')
    def validate_fields_that_can_not_be_none(cls, value, info: ValidationInfo):
        values_that_can_be_none = ['phone_number', 'address']
        if info.field_name not in values_that_can_be_none and value is None:
            raise ValueError(f"The given field {info.field_name} cannot be None.")
        return value


class CustomerCreateResource(CustomerBaseResource):
    pass

class CustomerUpdateResource(CustomerBaseResource):
    email: EmailStr = Field(
        default=None,
        description="Updated email of the customer.",
        examples=["henrik@gmail.com"]
    )
    phone_number: Optional[str] = Field(
        default=None,
        description="Updated phone number of the customer.",
        examples=["10203040"]
    )
    first_name: str = Field(
        default=None,
        description="Updated first name of the customer.",
        examples=["Henrik"]
    )
    last_name: str = Field(
        default=None,
        description="Updated last name of the customer.",
        examples=["Henriksen"]
    )
    address: Optional[str] = Field(
        default=None,
        description="Updated address of the customer.",
        examples=["Randomgade nr. 10 4. tv."]
    )

    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class CustomerReturnResource(CustomerBaseResource):
    id: str = Field(
        default=...,
        description="The UUID for the customer.",
        examples=["0ac1d668-55aa-46a1-898a-8fa61457facb"]
    )
