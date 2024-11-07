# External Library imports
import logging
from datetime import datetime
from fastapi import Depends, HTTPException, status
from jwt import ExpiredSignatureError, InvalidTokenError, encode, decode

# Internal library imports
from app.core.tokens import (
    SalesPersonReturnResource,
    TokenPayload,
    TokenData,
    Token
)
from app.core.config import (
    oauth2_mysql,
    pwd_context,
    SECRET_KEY,
    ALGORITHM
)

logger = logging.getLogger(__name__)


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
    encoded_jwt = encode(data.model_dump(), SECRET_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer", sales_person=sales_person)


def decode_access_token(token: str) -> TokenPayload:
    if not isinstance(token, str):
        raise TypeError(f"token must be of type str, not {type(token).__name__}.")
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub = payload.get("sub")
        exp = payload.get("exp")

        if not sub:
            raise InvalidTokenError("Missing subject in decoded token.")

        if exp is None:
            raise InvalidTokenError("Missing expiration in decoded token.")

        if not isinstance(exp, (int, float)):
            raise TypeError(
                f"""
                Expiration in decoded token is not an int or float, 
                but an invalid type of: {type(exp).__name__}."""
            )

        expires_at = datetime.utcfromtimestamp(exp)
        token_payload = TokenPayload(email=sub, expires_at=expires_at)
        return token_payload

    except ExpiredSignatureError as e:
        logger.error(
            msg=f"Could not validate credentials: Token has expired. {e}",
            exc_info=True,
            stack_info=True
        )
        raise e

    except InvalidTokenError as e:
        logger.error(
            msg=f"Could not validate credentials: Invalid token. {e}",
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
        detail="Internal server error.",
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
        logger.error(
            msg=f"Caught Exception in function get_current_sales_person_token in security.py: {e}",
            exc_info=True,
            stack_info=True
        )
        raise internal_server_error


async def get_current_mysql_sales_person_token(token: str = Depends(oauth2_mysql)):
    return get_current_sales_person_token(token)
