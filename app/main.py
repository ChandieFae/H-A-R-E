from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="H.A.R.E. – Human Abduction Response Engine",
    description="A rapid-response system for human abduction using geo-fencing, AI, and alerts.",
    version="0.1"
)

app.include_router(router)
from app.api.v1.router import router as api_router

app.include_router(api_router, prefix="/api/v1")
