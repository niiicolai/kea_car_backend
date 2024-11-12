import os
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_mysql = OAuth2PasswordBearer(tokenUrl="/mysql/token")
oauth2_mongodb = OAuth2PasswordBearer(tokenUrl="/mysql/token")
