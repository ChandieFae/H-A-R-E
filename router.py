from fastapi import APIRouter
from .endpoints import incidents

router = APIRouter()
router.include_router(incidents.router, prefix="/incident", tags=["Incident"])
