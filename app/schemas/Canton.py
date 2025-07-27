from pydantic import BaseModel

class CantonCreate(BaseModel):
    name: str