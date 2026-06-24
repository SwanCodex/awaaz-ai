from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    state = Column(String(100), nullable=False)

    eligibility = Column(Text, nullable=False)

    benefits = Column(Text, nullable=False)

    documents = Column(Text, nullable=False)