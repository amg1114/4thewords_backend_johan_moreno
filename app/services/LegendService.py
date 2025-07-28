from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from fastapi import HTTPException

from app.models import Legend, User, Category
from app.schemas import LegendCreate, LegendUpdate, LegendFilters
from app.services.ImageService import ImageService
from app.db.database import engine


class LegendService:
    @staticmethod
    def create(form_data: LegendCreate, user: User):
        image_url = ImageService.store_image(form_data.image)
        legend = Legend(
            name=form_data.name,
            description=form_data.description,
            date=form_data.date,
            category_id=form_data.category_id,
            district_id=form_data.district_id,
            publisher_id=user.id,
            image_url=image_url
        )

        with Session(engine) as session:
            session.add(legend)
            session.commit()
            session.refresh(legend)

        return legend

    @staticmethod
    def update(legend_id: int, form_data: LegendUpdate):
        with Session(engine) as session:
            legend = session.get(Legend, legend_id)
            if not legend:
                raise HTTPException(status_code=404, detail="Legend not found")

            # Dynamic field updates
            update_data = vars(form_data)
            print(f"Updating legend {legend_id} with data: {update_data}")
            for field, value in update_data.items():
                if field == "image" and value is not None:
                    ImageService.delete_image(legend.image_url)
                    print(f"Updating image for legend {legend_id}")
                    legend.image_url = ImageService.store_image(value)
                elif hasattr(legend, field) and value is not None:
                    setattr(legend, field, value)

            session.commit()
            session.refresh(legend)

        return legend

    @staticmethod
    def delete(legend_id: int):
        with Session(engine) as session:
            legend = session.get(Legend, legend_id)
            if not legend:
                raise HTTPException(status_code=404, detail="Legend not found")

            if legend.image_url:
                ImageService.delete_image(legend.image_url)

            session.delete(legend)
            session.commit()

            return {"detail": "Legend deleted successfully"}

    @staticmethod
    def get_all(filters: LegendFilters):
        with Session(engine) as session:
            legends = select(Legend).options(
                selectinload(Legend.publisher),
                selectinload(Legend.district),
                selectinload(Legend.canton),
                selectinload(Legend.province),
                selectinload(Legend.category)
            )

            if filters.name:
                legends = legends.where(Legend.name.ilike(f"%{filters.name}%"))

            if filters.category_id:
                legends = legends.where(
                    Legend.category_id == filters.category_id)

            if filters.date_from:
                legends = legends.where(Legend.date >= filters.date_from)

            if filters.date_to:
                legends = legends.where(Legend.date <= filters.date_to)

            if filters.district_id:
                legends = legends.where(
                    Legend.district_id == filters.district_id)
            
            if filters.canton_id:
                legends = legends.where(
                    Legend.canton_id == filters.canton_id)
            
            if filters.province_id:
                legends = legends.where(
                    Legend.province_id == filters.province_id)

            results = session.exec(legends).all()
            if not results:
                raise HTTPException(status_code=404, detail="No legends found")

            return results
    
    @staticmethod
    def get_by_id(legend_id: int):
        with Session(engine) as session:
            statement = (
                select(Legend)
                .where(Legend.id == legend_id)
                .options(
                    selectinload(Legend.publisher),
                    selectinload(Legend.district),
                    selectinload(Legend.canton),
                    selectinload(Legend.province),
                    selectinload(Legend.category),
                )
            )

            result = session.exec(statement).first()
            if not result:
                raise HTTPException(status_code=404, detail="Legend not found")
            return result
        
    @staticmethod
    def get_categories():
        with Session(engine) as session:
            categories = session.exec(select(Category)).all()
            if not categories:
                raise HTTPException(status_code=404, detail="No categories found")
            return categories