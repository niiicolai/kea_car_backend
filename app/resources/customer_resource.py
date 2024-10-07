from pydantic import BaseModel, ConfigDict, Field, field_validator

class CustomerBaseResource(BaseModel):
    email: str = Field(..., examples=["hans@gmail.com","lise@gmail.com"])
    phone_number: str | None = Field(None, examples=["10203040", None])
    first_name: str = Field(..., examples=["Hans", "Lise"])
    last_name: str = Field(..., examples=["Hansen", "Fiskesen"])
    address: str = Field(None, examples=[None, "Randomgade nr. 4 tv. Kbh 2100"])
    
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
    

class CustomerCreateResource(CustomerBaseResource):
    pass

class CustomerUpdateResource(CustomerBaseResource):
    email: str | None = Field(None, examples=["hans@gmail.com","lise@gmail.com"])
    first_name: str | None = Field(None, examples=["Hans", "Lise"])
    last_name: str | None = Field(None, examples=["Hansen", "Fiskesen"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class CustomerReturnResource(CustomerBaseResource):
    id: int = Field(..., examples=[1,2])