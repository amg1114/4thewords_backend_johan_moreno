from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import date

class Legend(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    date: date
    image_url: str
    district_id: Optional[int] = Field(default=None, foreign_key="district.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    publisher_id: Optional[int] = Field(default=None, foreign_key="user.id")
    