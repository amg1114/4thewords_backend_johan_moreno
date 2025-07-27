from fastapi import Form, UploadFile, File, HTTPException

from typing import Annotated
from datetime import datetime

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
