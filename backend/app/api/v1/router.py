from fastapi import APIRouter

from app.api.schemes import router as schemes_router

api_router = APIRouter()

api_router.include_router(schemes_router)