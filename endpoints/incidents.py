from fastapi import APIRouter
from app.models.schemas import Incident
from app.services.geo import calculate_radius_km

router = APIRouter()

@router.post("/incident")
def create_incident(incident: Incident):
    radius = calculate_radius_km(incident.mph, incident.minutes_elapsed)
    return {"radius_km": radius, "status": "search initialized"}
