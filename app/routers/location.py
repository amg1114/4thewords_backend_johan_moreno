from fastapi import APIRouter
from typing import List

from app.models import Province, District, Canton
from app.schemas import ProvinceCreate, CantonCreate, DistrictCreate
from app.services import LocationService

router = APIRouter(prefix="/location", tags=["Location"])
@router.get("/provinces", response_model=List[Province], summary="Get all provinces")
def register_province():
    return LocationService.get_all_provinces()

@router.post("/provinces", response_model=Province, summary="Create a new province")
def create_province(province_data: ProvinceCreate):
    return LocationService.create_province(province_data)

@router.get("/{id}/districts", response_model=List[District], summary="Get all districts for a province by ID")
def get_districts_by_province_id(id: int):
    return LocationService.get_districts_by_province_id(id)

@router.post("/{id}/districts", response_model=District, summary="Create a new district for a province by ID")
def get_districts_by_province_id(id: int, district_data: DistrictCreate):
    return LocationService.create_district(id, district_data)

@router.get("/{id}/cantons", response_model=List[Canton], summary="Get all cantons for a district by ID")
def get_cantons_by_district_id(id: int):
    return LocationService.get_cantons_by_district_id(id)

@router.post("/{id}/cantons", response_model=Canton, summary="Create a new canton for a district by ID")
def get_cantons_by_district_id(id: int, canton_data: CantonCreate):
    return LocationService.create_canton(id, canton_data)
