from pydantic import BaseModel

class ProvinceCreate(BaseModel):
    name: str
    
class ProvinceRead(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }