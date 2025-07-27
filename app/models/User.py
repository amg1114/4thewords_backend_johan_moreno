from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from app.models import Legend

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    
    legends: List["Legend"] = Relationship(back_populates="publisher")