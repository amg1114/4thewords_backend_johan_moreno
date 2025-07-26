from sqlmodel import Field, SQLModel
from typing import Optional

class Canton(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    codigo: str = Field(index=True, unique=True)
    provincia_id: Optional[int] = Field(default=None, foreign_key="provincia.id")