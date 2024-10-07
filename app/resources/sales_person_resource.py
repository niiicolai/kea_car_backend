from pydantic import BaseModel, ConfigDict, Field, field_validator

class SalesPersonBaseResource(BaseModel):
    first_name: str = Field(..., examples=["Tom", "Pia"])
    last_name: str = Field(..., examples=["Thomsen", "Pil"])
    
    model_config = ConfigDict(from_attributes=True)
    
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
    
class SalesPersonValidationResource(SalesPersonBaseResource):
    employee_number: str = Field(..., examples=["abcedf", "fdecba"])
    
    @field_validator('employee_numbe')
    def validate_employee_number(cls, value: str) -> str:
        value = value.strip()
        if len(value) != 6:
            raise ValueError(f"The given employee number {value} is not six characters.")
        return value
    
    

class SalesPersonCreateResource(SalesPersonBaseResource):
    pass

class SalesPersonUpdateResource(SalesPersonBaseResource):
    first_name: str | None = Field(None, examples=["Tom", "Pia"])
    last_name: str | None = Field(None, examples=["Thomsen", "Pil"])
    
    def get_updated_fields(self) -> dict:
        return self.model_dump(exclude_unset=True)

class SalesPersonReturnResource(SalesPersonValidationResource):
    id: int = Field(..., examples=[1,2])
    