from fastapi import Query
from pydantic import BaseModel
from typing import Optional
from datetime import date

class LegendFilters(BaseModel):
    name: Optional[str] = Query(None, description="Filtering by legend name")
    date_from: Optional[date] = Query(None, description="Filtering by start date")
    date_to: Optional[date] = Query(None, description="Filtering by end date")
    category_id: Optional[int] = Query(None, description="Filtering by category ID")
    province_id: Optional[int] = Query(None, description="Filtering by province ID")
    canton_id: Optional[int] = Query(None, description="Filtering by canton ID")
    district_id: Optional[int] = Query(None, description="Filtering by district ID")