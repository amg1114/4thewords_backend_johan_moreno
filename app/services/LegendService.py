from sqlmodel import Session

from app.models import Legend, User
from app.schemas import LegendCreate
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