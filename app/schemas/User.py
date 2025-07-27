from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class UserRead(SQLModel):
    id: int
    name: str
    email: str
    
    model_config = {
       "from_attributes": True
    }