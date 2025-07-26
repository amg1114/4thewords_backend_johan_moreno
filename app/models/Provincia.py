from sqlmodel import Field, SQLModel


class Provincia(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str