from pydantic import BaseModel

class DistrictCreate(BaseModel):
    name: str