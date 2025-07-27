from sqlmodel import Field, SQLModel


class Province(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str