from sqlmodel import Session, select
from fastapi import HTTPException

from app.db.database import engine
from app.schemas import ProvinceCreate, CantonCreate, DistrictCreate
from app.models import Province, District, Canton

class LocationService:
    @staticmethod
    def get_all_provinces():
        with Session(engine) as session:
            provinces = session.exec(select(Province)).all()

            if not provinces:
                raise HTTPException(
                    status_code=404, detail="No provinces found")

            return provinces

    @staticmethod
    def get_province_by_id(province_id: int):
        with Session(engine) as session:
            province = session.get(Province, province_id)

            if not province:
                raise HTTPException(
                    status_code=404, detail="Province not found")

            return province

    @staticmethod
    def create_province(province_data: ProvinceCreate):
        with Session(engine) as session:
            new_province = Province(**province_data.model_dump())
            session.add(new_province)
            session.commit()
            session.refresh(new_province)

            return new_province

    @staticmethod
    def get_cantons_by_province_id(province_id: int):
        with Session(engine) as session:
            cantons = session.exec(select(Canton).where(
                Canton.province_id == province_id)).all()

            if not cantons:
                raise HTTPException(
                    status_code=404, detail="No cantons found for this district")

            return cantons
        
    @staticmethod
    def get_canton_by_id(canton_id: int):
        with Session(engine) as session:
            canton = session.get(Canton, canton_id)

            if not canton:
                raise HTTPException(
                    status_code=404, detail="Canton not found")

            return canton

    @staticmethod
    def create_canton(province_id: int, canton_data: CantonCreate):
        with Session(engine) as session:
            province = LocationService.get_province_by_id(province_id)

            if not province:
                raise HTTPException(
                    status_code=404, detail="Province not found")

            new_canton = Canton(name=canton_data.name, province_id=province.id)
            session.add(new_canton)
            session.commit()
            session.refresh(new_canton)

            return new_canton
    
    @staticmethod
    def get_districts_by_canton_id(province_id: int):
        with Session(engine) as session:
            districts = session.exec(select(District).where(
                District.canton_id == province_id)).all()

            if not districts:
                raise HTTPException(
                    status_code=404, detail="No districts found for this province")

            return districts

    @staticmethod
    def get_district_by_id(district_id: int):
        with Session(engine) as session:
            district = session.get(District, district_id)

            if not district:
                raise HTTPException(
                    status_code=404, detail="District not found")

            return district

    @staticmethod
    def create_district(canton_id: int, district_data: DistrictCreate):
        with Session(engine) as session:
            canton = LocationService.get_canton_by_id(canton_id)
            if not canton:
                raise HTTPException(status_code=404, detail="Canton not found")

            new_district = District(name=district_data.name, canton_id=canton.id)
            session.add(new_district)
            session.commit()
            session.refresh(new_district)

            return new_district
