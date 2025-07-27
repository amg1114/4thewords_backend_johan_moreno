from fastapi import APIRouter, Depends
from typing import Annotated

from app.models import Legend, User
from app.schemas import LegendCreate, LegendUpdate, LegendRead, parse_legend_create, parse_legend_update
from app.services import LegendService, AuthService

router = APIRouter(prefix="/legend", tags=["Legend"])

@router.get("/", response_model=list[LegendRead], summary="Get all legends")
def get_all():
    legend_service = LegendService()
    return legend_service.get_all()

@router.post("/", response_model=Legend, summary="Create a new legend")
def create(form_data: Annotated[LegendCreate, Depends(parse_legend_create)], user: User = Depends(AuthService.get_current_user)):
    legend_service = LegendService()
    return legend_service.create(form_data, user)

@router.patch("/{legend_id}", response_model=Legend, summary="Update an existing legend")
def update(legend_id: int, form_data: Annotated[LegendUpdate, Depends(parse_legend_update)], user: User = Depends(AuthService.get_current_user)):
    legend_service = LegendService()
    return legend_service.update(legend_id, form_data)

@router.delete("/{legend_id}", summary="Delete a legend")
def delete(legend_id: int, user: User = Depends(AuthService.get_current_user)):
    legend_service = LegendService()
    legend_service.delete(legend_id)
    return {"detail": "Legend deleted successfully"}