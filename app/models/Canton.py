from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from app.models import District, Legend

class Canton(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    legends: List["Legend"] = Relationship(back_populates="canton")