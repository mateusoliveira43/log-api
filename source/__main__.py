"""Log API."""

from fastapi import APIRouter, FastAPI

from source import __version__
from source.routes import customer, event, user

log_api = FastAPI(
    title="Log API's endpoints documentation",
    version=__version__,
    description="List of all service's endpoints.",
    openapi_url="/api/openapi.json",
    docs_url="/docs",
    redocs_url=None,
)

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(customer.router)
api_router.include_router(event.router)

log_api.include_router(api_router)
