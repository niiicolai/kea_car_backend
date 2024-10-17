from datetime import datetime, timedelta
import logging
from sqlalchemy.orm import Session
from typing import Optional, Union
from jose import JWTError, jwt
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.sales_person import SalesPerson
from app.resources.sales_person_resource import SalesPersonLoginResource
from abc import ABC, abstractmethod

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = logging.getLogger(__name__)

class TokenPayload(BaseModel):
    email: str = Field(..., alias="sub")
    expires_at: datetime = Field(..., alias="exp")


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: str = Field(..., alias="sub")
    exp: int = Field(default_factory=lambda: (
        (datetime.utcnow() + timedelta(
            minutes=(ACCESS_TOKEN_EXPIRE_MINUTES if ACCESS_TOKEN_EXPIRE_MINUTES is not None else 15)))
    ))

class SalesPersonRepository(ABC):
    @abstractmethod
    def fetch_by_email(self, email: str) -> Optional[SalesPerson]:
        pass


class MySQLSalesPersonRepository(SalesPersonRepository):
    def __init__(self, session: Session):
        self.session = session

    def fetch_by_email(self, email: str) -> Optional[SalesPerson]:
        return self.session.query(SalesPerson).filter_by(email=email).first()


# Placeholder for future repositories
# class OtherDBSalesPersonRepository(SalesPersonRepository):
#     ...

def verify_sales_person_email(
        sent_sales_person_login_info: SalesPersonLoginResource,
        repository: SalesPersonRepository
) -> Optional[SalesPerson]:
    return repository.fetch_by_email(sent_sales_person_login_info.email)

def verify_password(
        sent_sales_person_login_info: SalesPersonLoginResource,
        found_sales_person_in_db: Union[SalesPerson]
) -> bool:

    sent_login_password = sent_sales_person_login_info.password
    if isinstance(found_sales_person_in_db, SalesPerson):
        hashed_password = found_sales_person_in_db.password
    else:
        return False
    return pwd_context.verify(sent_login_password, hashed_password)


def get_password_hash(password: str) -> Optional[str]:
    if not isinstance(password, str):
        return None
    return pwd_context.hash(password)


def create_access_token(sales_person: Union[SalesPerson]) -> Optional[str]:
    if isinstance(sales_person, SalesPerson):
        email = sales_person.email
    else:
        return None
    data: TokenData = TokenData(sub=email)
    encoded_jwt = jwt.encode(data.model_dump(), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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
            expires_at = datetime.utcfromtimestamp(expires_at)
        return TokenPayload(
            email=email,
            expires_at=expires_at)
    except JWTError as e:
        logger.error(
            f"Could not validate credentials: Invalid token. {e}",
            exc_info=True,
            stack_info=True
        )
        return None