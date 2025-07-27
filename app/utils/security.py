from datetime import datetime, timedelta
from typing import Optional

from passlib.context import CryptContext
from dotenv import load_dotenv
from jose import JWTError, jwt

from app.models import User
import os

load_dotenv()

try:
   JWT_SECRET = os.environ["JWT_SECRET"]
   JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
   JWT_EXPIRATION = int(os.environ["JWT_EXPIRATION"])
except KeyError as e:
    raise RuntimeError(f"🚨 DB env var is missing: {e}")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str, user: User) -> bool:
    if not verify_password(password, user.password):
        return False
    return True

def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.now() + (expires_delta or timedelta(minutes=JWT_EXPIRATION))
    
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return encoded_jwt

def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise None