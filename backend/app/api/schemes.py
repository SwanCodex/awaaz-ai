from fastapi import APIRouter

router = APIRouter(
    prefix="/api/schemes",
    tags=["Schemes"]
)


@router.get("/")
def get_schemes():
    return [
        {
            "id": 1,
            "name": "PM Kisan Samman Nidhi",
            "state": "All India",
            "benefits": "Financial assistance for farmers"
        },
        {
            "id": 2,
            "name": "Mahatma Jyotiba Phule Jan Arogya Yojana",
            "state": "Maharashtra",
            "benefits": "Health insurance coverage"
        }
    ]