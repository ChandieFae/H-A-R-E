from pydantic import BaseModel

class Incident(BaseModel):
    origin_lat: float
    origin_lng: float
    minutes_elapsed: int
    mph: int
    vehicle_description: str = None
    suspect_description: str = None
