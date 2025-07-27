from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

from app.models import Legend, Canton

class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    canton_id: Optional[int] = Field(default=None, foreign_key="canton.id")
    
    canton: Optional["Canton"] = Relationship(back_populates="districts")
    legends: list["Legend"] = Relationship(back_populates="district")