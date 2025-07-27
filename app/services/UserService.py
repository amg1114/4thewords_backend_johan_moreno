from sqlmodel import Session, select
from fastapi import HTTPException

from app.db.database import engine
from app.models import User
from app.schemas import UserCreate, UserRead
from app.utils.security import hash_password

class UserService:    
    @staticmethod
    def create(data: UserCreate) -> User:
        with Session(engine) as session:
            if session.exec(select(User).where(User.email == data.email)).first():
                raise HTTPException(
                    status_code=400,
                    detail="Email already registered"
                )
            
            hashed_password = hash_password(data.password)
            user = User(
                name=data.name,
                email=data.email,
                password=hashed_password
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        
    @staticmethod
    def find_by_email(email: str) -> User:
        with Session(engine) as session:
            user = session.exec(select(User).where(User.email == email)).first()
            if not user:
                raise HTTPException(
                    status_code=404,
                    detail="User not found"
                )
            return user