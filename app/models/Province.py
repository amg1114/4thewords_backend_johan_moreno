from sqlmodel import Field, SQLModel, Relationship
from typing import List

from app.models import Canton, Legend

class Province(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    
    legends: List["Legend"] = Relationship(back_populates="province")