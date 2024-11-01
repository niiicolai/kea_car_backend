# External Library imports
import logging
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from typing import Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

# Internal library imports
from app.resources.sales_person_resource import SalesPersonReturnResource
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context, oauth2_mysql

logger = logging.getLogger(__name__)


class TokenPayload(BaseModel):
    email: str = Field(..., examples=["hans@gmail.com"])
    expires_at: datetime = Field(...,
                                 examples=[(datetime.utcnow() + timedelta(minutes=15)).strftime("%Y-%m-%dT%H:%M:%S")])


class Token(BaseModel):
    access_token: str = Field(..., examples=[
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdXNhbiIsImV4cCI6MTcyOTE2NTEyOX0.U1wCg1dyIX2U1dSjLHSpi3EGc99lXK1458G8j39TCiw"])
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
    if sent_email == sales_person_resource.email:
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
    encoded_jwt = jwt.encode(data.dict(), SECRET_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer", sales_person=sales_person)


def decode_access_token(token: str) -> TokenPayload:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub: Optional[str] = payload.get("sub")
        if sub is None:
            raise InvalidTokenError("Missing subject in decoded token.")
        exp: Union[int, float, None] = payload.get("exp")
        if exp is None:
            raise InvalidTokenError("Missing expiration in decoded token.")
        if isinstance(exp, int) or isinstance(exp, float):
            expires_at: datetime = datetime.utcfromtimestamp(exp)
            token_payload = TokenPayload(email=sub, expires_at=expires_at)
            return token_payload
        else:
            raise ValueError("Expiration in decoded token is not an integer or a float.")
    except ExpiredSignatureError as e:
        logger.error(
            f"Could not validate credentials: Token has expired. {e}",
            exc_info=True,
            stack_info=True
        )
        raise e
    except InvalidTokenError as e:
        logger.error(
            f"Could not validate credentials: Invalid token. {e}",
            exc_info=True,
            stack_info=True
        )
        raise e


def get_current_sales_person_token(token: str) -> TokenPayload:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    internal_server_error = HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Internal server error",
    )
    try:
        token_payload = decode_access_token(token)
        return token_payload
    except ExpiredSignatureError:
        credentials_exception.detail += ": Token has expired."
        raise credentials_exception
    except InvalidTokenError:
        credentials_exception.detail += ": Invalid token."
        raise credentials_exception
    except Exception as e:
        internal_server_error.detail += f": {e}."
        raise internal_server_error


async def get_current_mysql_sales_person_token(token: str = Depends(oauth2_mysql)):
    return get_current_sales_person_token(token)
