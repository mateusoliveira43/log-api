"""Log API."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from source import __version__
from source.routes import router

log_api = FastAPI(
    title="Log API's endpoints documentation",
    version=__version__,
    description="List of all service's endpoints.",
    openapi_url="/api/openapi.json",
    docs_url="/docs",
    redocs_url=None,
)


@log_api.exception_handler(SQLAlchemyError)
async def handle_sqlalchemy_exceptions(
    request: Request, exc: SQLAlchemyError  # pylint: disable=unused-argument
) -> JSONResponse:
    """
    Handle SQLAlchemy exceptions.

    Parameters
    ----------
    request : starlette.requests.Request
        API request.
    exc : sqlalchemy.exc.SQLAlchemyError
        Raised Exception from API.

    Returns
    -------
    starlette.responses.JSONResponse
        Handled exception.

    """
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc.orig).strip()},
    )


log_api.include_router(router)
