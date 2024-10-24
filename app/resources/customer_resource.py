from pydantic import BaseModel, ConfigDict, Field, UUID4, ValidationInfo, field_validator, EmailStr
from typing import Optional

class CustomerBaseResource(BaseModel):
    email: EmailStr = Field(..., examples=["henrik@gmail.com"])
    phone_number: Optional[str] = Field(..., examples=["10203040"])
    first_name: str = Field(..., examples=["'Henrik"])
    last_name: str = Field(..., examples=["Henriksen"])
    address: Optional[str] = Field(..., examples=["Randomgade nr. 10 4. tv."])
    
    model_config = ConfigDict(from_attributes=True)

    
    @field_validator('phone_number')
    def validate_phone_number(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given phone number {value} is an empty string.")
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
    
    @field_validator('address')
    def validate_address(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given address {value} is an empty string.")
        return value

    @field_validator('*', mode='before')
    def validate_fields_that_can_not_be_none(cls, value, info: ValidationInfo):
        values_that_can_be_none = ['phone_number', 'address']
        if info.field_name not in values_that_can_be_none and value is None:
            raise ValueError(f"The given field {info.field_name} cannot be None.")
        return value


class CustomerCreateResource(CustomerBaseResource):
    pass

class CustomerUpdateResource(CustomerBaseResource):
    email: EmailStr = Field(None, examples=["henrik@gmail.com"])
    phone_number: Optional[str] = Field(None, examples=["10203040"])
    first_name: str = Field(None, examples=["Henrik"])
    last_name: str = Field(None, examples=["Henriksen"])
    address: Optional[str] = Field(None, examples=["Randomgade nr. 10 4. tv."])

    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class CustomerReturnResource(CustomerBaseResource):
    id: str = Field(..., examples=["0ac1d668-55aa-46a1-898a-8fa61457facb"])