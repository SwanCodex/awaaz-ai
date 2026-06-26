from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend services for Awaaz-AI"
)

logger.info("Starting Awaaz-AI Backend")
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Awaaz-AI Backend Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

