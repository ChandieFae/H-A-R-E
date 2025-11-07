from fastapi import APIRouter
from app.models import Incident
from app.geo import calculate_radius_km

router = APIRouter()

@router.post("/incident")
def create_incident(incident: Incident):
    radius_km = calculate_radius_km(incident.mph, incident.minutes_elapsed)
    return {
        "message": "Incident received.",
        "search_radius_km": radius_km
    }
