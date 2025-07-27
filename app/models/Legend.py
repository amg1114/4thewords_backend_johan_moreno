from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import date

from app.models import User, District, Category

class Legend(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    date: date
    image_url: str
    
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    district_id: Optional[int] = Field(default=None, foreign_key="district.id")
    publisher_id: Optional[int] = Field(default=None, foreign_key="user.id")
    
    publisher: Optional["User"] = Relationship(back_populates="legends")
    district: Optional["District"] = Relationship(back_populates="legends")
    category: Optional["Category"] = Relationship(back_populates="legends")