from pydantic import BaseModel
from sqlmodel import SQLModel
class DistrictCreate(BaseModel):
    name: str
    
class DistrictRead(BaseModel):
    id: int
    name: str
    
    model_config = {
        "from_attributes": True
    }