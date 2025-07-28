from fastapi import APIRouter
from typing import List

from app.models import Province, District, Canton
from app.schemas import ProvinceCreate, CantonCreate, DistrictCreate
from app.services import LocationService

router = APIRouter(prefix="/location", tags=["Location"])


@router.get("/provinces", response_model=List[Province], summary="Get all provinces")
def get_provinces():
    return LocationService.get_all_provinces()


@router.post("/provinces", response_model=Province, summary="Create a new province")
def create_province(province_data: ProvinceCreate):
    return LocationService.create_province(province_data)


@router.get("/districts", response_model=List[District], summary="Get all districts")
def get_districts():
    return LocationService.get_districts()


@router.post("/districts", response_model=District, summary="Create a new district")
def create_district(district_data: DistrictCreate):
    return LocationService.create_district(district_data)


@router.get("/cantons", response_model=List[Canton], summary="Get all cantons")
def get_cantons():
    return LocationService.get_cantons()


@router.post("/cantons", response_model=Canton, summary="Create a new canton")
def create_canton(canton_data: CantonCreate):
    return LocationService.create_canton(canton_data)
