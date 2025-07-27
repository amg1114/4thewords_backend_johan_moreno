from sqlmodel import Field, SQLModel
from typing import Optional

class Canton(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    province_id: Optional[int] = Field(default=None, foreign_key="province.id")