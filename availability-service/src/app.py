from fastapi import FastAPI
from src.routes import availability_routes
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Availability Service")

app.include_router(availability_routes.router, prefix="/availability", tags=["Availability"])

Instrumentator().instrument(app).expose(app)
