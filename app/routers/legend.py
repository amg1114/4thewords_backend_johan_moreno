from fastapi import APIRouter, Depends
from typing import Annotated

from app.models import Legend, User
from app.schemas.Legend import LegendCreate, parse_legend_create
from app.services import LegendService, AuthService

router = APIRouter(prefix="/legend", tags=["Legend"])

@router.post("/", response_model=Legend, summary="Create a new legend")
def create(form_data: Annotated[LegendCreate, Depends(parse_legend_create)], user: User = Depends(AuthService.get_current_user)):
    legend_service = LegendService()
    return legend_service.create(form_data, user)
