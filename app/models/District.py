from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

from app.models import Legend

class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    legends: list["Legend"] = Relationship(back_populates="district")