# External Library imports
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

# Internal library imports
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.resources.sales_person_resource import SalesPersonReturnResource


class TokenPayload(BaseModel):
    email: str = Field(
        default=...,
        description="The email of the sales person that the token belongs to.",
        examples=["hans@gmail.com"]
    )
    expires_at: datetime = Field(
        default=...,
        description="The date and time as UTC for when the token expires.",
        examples=
        [
            (datetime.utcnow() + timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%S")
        ]
    )


class Token(BaseModel):
    access_token: str = Field(
        default=...,
        description="The access token needed for accessing endpoints that requires authorization.",
        examples=[
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
            "eyJzdWIiOiJzdXNhbiIsImV4cCI6MTcyOTE2NTEyOX0."
            "U1wCg1dyIX2U1dSjLHSpi3EGc99lXK1458G8j39TCiw"
        ]
    )
    token_type: str = Field(
        default=...,
        description="The type of token that is needed for authorization.",
        examples=["bearer"]
    )
    sales_person: SalesPersonReturnResource = Field(
        default=...,
        description="The sales person that the token belongs to."
    )


class TokenData(BaseModel):
    sub: str = Field(default=...)
    exp: datetime = Field(
        default_factory=lambda: ((datetime.utcnow() + timedelta(
            minutes=(ACCESS_TOKEN_EXPIRE_MINUTES if ACCESS_TOKEN_EXPIRE_MINUTES is not None else 15)
        )))
    )
