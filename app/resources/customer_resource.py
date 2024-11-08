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
        if email is None:
            raise ValueError("The given email cannot be set to None.")
        return email
    
    @field_validator('phone_number')
    def validate_phone_number(cls, phone_number: Optional[str]) -> Optional[str]:
        if phone_number is not None:
            value = phone_number.strip()
            if len(value) == 0:
                raise ValueError(f"The given phone number {phone_number} is an empty string.")
        return phone_number
    
    @field_validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        if first_name is None:
            raise ValueError("The given first name cannot be set to None.")
        first_name = first_name.strip()
        if len(first_name) == 0:
            raise ValueError(f"The given first name {first_name} is an empty string.")
        return first_name
    
    @field_validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        if last_name is None:
            raise ValueError("The given last name cannot be set to None.")
        last_name = last_name.strip()
        if len(last_name) == 0:
            raise ValueError(f"The given last name {last_name} is an empty string.")
        return last_name
    
    @field_validator('address')
    def validate_address(cls, address: Optional[str]) -> Optional[str]:
        if address is not None:
            address = address.strip()
            if len(address) == 0:
                raise ValueError(f"The given address {address} is an empty string.")
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
