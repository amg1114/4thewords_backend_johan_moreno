from sqlmodel import Field, SQLModel, Relationship
from typing import List

from app.models import Canton

class Province(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    
    cantons: List["Canton"] = Relationship(back_populates="province")