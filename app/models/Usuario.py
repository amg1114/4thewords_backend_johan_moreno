from sqlmodel import Field, SQLModel
from typing import Optional

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str = Field(index=True, unique=True)
    password: str