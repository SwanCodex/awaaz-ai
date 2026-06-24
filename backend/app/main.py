from fastapi import FastAPI

from app.core.config import settings
from app.api.schemes import router as scheme_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend services for Awaaz-AI"
)

app.include_router(scheme_router)

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

