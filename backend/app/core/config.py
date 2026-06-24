from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Awaaz-AI"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/awaaz_ai"

    class Config:
        env_file = ".env"


settings = Settings()