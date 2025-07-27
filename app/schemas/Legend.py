from fastapi import Form, UploadFile, File, HTTPException
from sqlmodel import SQLModel
from typing import Annotated, Optional
from datetime import datetime, date

from app.schemas import UserRead, CategoryRead, DistrictRead

class LegendCreate:
    def __init__(
        self,
        name,
        description,
        date,
        category_id,
        district_id,
        image
    ):
        if not image.content_type.startswith("image/"):
            raise HTTPException("File must be an image")

        self.name = name
        self.description = description
        self.category_id = category_id
        self.district_id = district_id
        self.image = image
        self.date = date

class LegendRead(SQLModel):
    id: int
    name: str
    description: str
    date: date
    image_url: str
    
    publisher: Optional[UserRead]
    category: Optional[CategoryRead]
    district: Optional[DistrictRead]

def parse_legend_create(
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    date: Annotated[str, Form()],
    category_id: Annotated[int, Form()],
    district_id: Annotated[int, Form()],
    image: Annotated[UploadFile, File()]
) -> LegendCreate:
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()

    return LegendCreate(name, description, parsed_date, category_id, district_id, image)


class LegendUpdate:
    def __init__(
        self,
        name: str = None,
        description: str = None,
        date: datetime = None,
        category_id: int = None,
        district_id: int = None,
        image: UploadFile = None
    ):
        self.name = name
        self.description = description
        self.date = date
        self.category_id = category_id
        self.district_id = district_id
        self.image = image


def parse_legend_update(
    name: Annotated[str, Form()] = None,
    description: Annotated[str, Form()] = None,
    date: Annotated[str, Form()] = None,
    category_id: Annotated[int, Form()] = None,
    district_id: Annotated[int, Form()] = None,
    image: Annotated[UploadFile, File()] = None
) -> LegendUpdate:
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date() if date else None
    return LegendUpdate(name, description, parsed_date, category_id, district_id, image)
