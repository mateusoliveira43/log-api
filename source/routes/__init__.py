"""Service endpoints."""

from fastapi import APIRouter

from source.routes import customer, event, user

router = APIRouter()

router.include_router(user.router)
router.include_router(customer.router)
router.include_router(event.router)
