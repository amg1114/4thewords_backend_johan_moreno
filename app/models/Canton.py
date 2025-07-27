from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from app.models import District, Province

class Canton(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    province_id: Optional[int] = Field(default=None, foreign_key="province.id")
    
    
    province : Optional["Province"] = Relationship(back_populates="cantons")
    districts: List["District"] = Relationship(back_populates="canton")