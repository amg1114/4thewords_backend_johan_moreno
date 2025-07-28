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
    def create_province(province_data: ProvinceCreate):
        with Session(engine) as session:
            new_province = Province(**province_data.model_dump())
            session.add(new_province)
            session.commit()
            session.refresh(new_province)

            return new_province

    @staticmethod
    def get_cantons():
        with Session(engine) as session:
            cantons = session.exec(select(Canton)).all()

            if not cantons:
                raise HTTPException(
                    status_code=404, detail="No cantons found")

            return cantons

    @staticmethod
    def create_canton(canton_data: CantonCreate):
        with Session(engine) as session:

            new_canton = Canton(name=canton_data.name)
            session.add(new_canton)
            session.commit()
            session.refresh(new_canton)

            return new_canton

    @staticmethod
    def get_districts():
        with Session(engine) as session:
            districts = session.exec(select(District)).all()

            if not districts:
                raise HTTPException(
                    status_code=404, detail="No districts found")

            return districts

    @staticmethod
    def create_district(district_data: DistrictCreate):
        with Session(engine) as session:

            new_district = District(
                name=district_data.name)
            session.add(new_district)
            session.commit()
            session.refresh(new_district)

            return new_district
