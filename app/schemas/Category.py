from sqlmodel import SQLModel

class CategoryRead(SQLModel):
    id: int
    name: str
    description: str

    model_config = {
        "from_attributes": True
    }