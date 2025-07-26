from sqlmodel import Field, SQLModel
from typing import Optional

class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str