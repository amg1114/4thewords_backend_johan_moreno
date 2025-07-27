from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

from app.models import Legend


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str

    legends: List["Legend"] = Relationship(
        back_populates="category")