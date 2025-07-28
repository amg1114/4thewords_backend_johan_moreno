from pydantic import BaseModel

class CantonCreate(BaseModel):
    name: str
    
class CantonRead(BaseModel):
    id: int
    name: str
    
    model_config = {
        "from_attributes": True
    }