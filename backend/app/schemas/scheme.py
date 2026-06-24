from pydantic import BaseModel


class SchemeBase(BaseModel):
    name: str
    state: str
    eligibility: str
    benefits: str
    documents: str


class SchemeResponse(SchemeBase):
    id: int

    model_config = {
        "from_attributes": True
    }