from pydantic import BaseModel, ConfigDict, Field, ValidationInfo, field_validator
from typing import Optional

class CustomerBaseResource(BaseModel):
    email: str = Field(..., examples=["hans@gmail.com","lise@gmail.com"])
    phone_number: Optional[str] = Field(..., examples=["10203040", None])
    first_name: str = Field(..., examples=["Hans", "Lise"])
    last_name: str = Field(..., examples=["Hansen", "Fiskesen"])
    address: Optional[str] = Field(..., examples=[None, "Randomgade nr. 4 tv. Kbh 2100"])
    
    model_config = ConfigDict(from_attributes=True)


    @field_validator('email')
    def validate_email(cls, value: str) -> str:
        if value is not None:
            value = value.strip()
            if len(value) == 0:
                raise ValueError(f"The given email {value} is an empty string.")
        return value
    
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
    email: str = Field(None, examples=["hans@gmail.com","lise@gmail.com"])
    phone_number: Optional[str] = Field(None, examples=["10203040", None])
    first_name: str = Field(None, examples=["Hans", "Lise"])
    last_name: str = Field(None, examples=["Hansen", "Fiskesen"])
    address: Optional[str] = Field(None, examples=["Randomgade nr. 4 tv. Kbh 2100"])

    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class CustomerReturnResource(CustomerBaseResource):
    id: int = Field(..., examples=[1,2])