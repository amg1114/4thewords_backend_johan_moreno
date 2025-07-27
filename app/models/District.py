from sqlmodel import SQLModel, Field
from typing import Optional

class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    canton_id: Optional[int] = Field(default=None, foreign_key="canton.id")