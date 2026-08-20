"""Provided FastAPI course shell; capstone routes intentionally return 501."""

from fastapi import FastAPI

from app.api import (
    auth_routes,
    automation_routes,
    campaign_routes,
    health_routes,
    tutorial_routes,
)
from app.api_models import MessageResponse
from app.config import get_settings

settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version="0.1.0-workshop",
    summary="Build a functional fusion-materials discovery API chapter by chapter",
    description=(
        "Start with GET /v1/tutorials. Capstone routes intentionally return HTTP 501 "
        "until their referenced chapter acceptance criteria are complete. Bundled "
        "material properties are synthetic and are not reactor-qualification data."
    ),
    swagger_ui_parameters={"persistAuthorization": True, "displayRequestDuration": True},
)

app.include_router(health_routes.router)
app.include_router(tutorial_routes.router)
app.include_router(auth_routes.router)
app.include_router(campaign_routes.router)
app.include_router(automation_routes.router)


@app.get("/", response_model=MessageResponse, tags=["Health"])
def root() -> MessageResponse:
    return MessageResponse(message="Open /docs, then begin with GET /v1/tutorials")
