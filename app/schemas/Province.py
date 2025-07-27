from pydantic import BaseModel

class ProvinceCreate(BaseModel):
    name: str