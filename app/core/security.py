from datetime import datetime, timedelta
import logging
from typing import Optional, Union
from jose import JWTError, jwt
from pydantic import BaseModel, Field
from fastapi import Depends, HTTPException, status
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context, oauth2_mysql
from app.resources.sales_person_resource import SalesPersonReturnResource

logger = logging.getLogger(__name__)

class TokenPayload(BaseModel):
    email: str = Field(..., examples=["hans@gmail.com"])
    expires_at: datetime = Field(..., examples=[(datetime.utcnow() + timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%S")])


class Token(BaseModel):
    access_token: str = Field(..., examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdXNhbiIsImV4cCI6MTcyOTE2NTEyOX0.U1wCg1dyIX2U1dSjLHSpi3EGc99lXK1458G8j39TCiw"])
    token_type: str = Field(..., examples=["bearer"])
    sales_person: SalesPersonReturnResource = Field(...)

class TokenData(BaseModel):
    sub: str = Field(...)
    exp: datetime = Field(default_factory=lambda: (
        (datetime.utcnow() + timedelta(
            minutes=(ACCESS_TOKEN_EXPIRE_MINUTES if ACCESS_TOKEN_EXPIRE_MINUTES is not None else 15)))
    ))


def verify_sales_person_email(
        sent_email: str,
        sales_person_resource: SalesPersonReturnResource
) -> bool:
    if sent_email == sales_person_resource.email :
        return True
    return False

def verify_password(
        sent_login_password: str,
        found_hashed_password: str
) -> bool:
    return pwd_context.verify(sent_login_password, found_hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(sales_person: SalesPersonReturnResource) -> Token:
    email = sales_person.email
    data: TokenData = TokenData(sub=email)
    encoded_jwt = jwt.encode(data.model_dump(), SECRET_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer", sales_person=sales_person)


def decode_access_token(token: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: Optional[str] = payload.get("sub")
        if email is None:
            raise JWTError("Missing subject in decoded token.")
        expires_at: Union[int, datetime, None] = payload.get("exp")
        if expires_at is None:
            raise JWTError("Missing expiration in decoded token.")
        if isinstance(expires_at, int):
            expires_at: datetime = datetime.utcfromtimestamp(expires_at)
        token_payload = TokenPayload(email=email, expires_at=expires_at)
        return token_payload
    except JWTError as e:
        logger.error(
            f"Could not validate credentials: Invalid token. {e}",
            exc_info=True,
            stack_info=True
        )
    return None



def get_current_sales_person_token(token: str) -> TokenPayload:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_payload = decode_access_token(token)
    if token_payload is None:
        credentials_exception.detail += ": Invalid token, payload is None."
        raise credentials_exception

    if token_payload.expires_at < datetime.utcnow():
        credentials_exception.detail += ": Token has expired."
        raise credentials_exception

    return token_payload

async def get_current_mysql_sales_person_token(token: str = Depends(oauth2_mysql)):
    return get_current_sales_person_token(token)