import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from sqlalchemy import URL


load_dotenv()


class AppSettings(BaseSettings):
    SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")

    DATABASE_USER: str = os.getenv("POSTGRES_USER", "admin")
    DATABASE_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = os.getenv("DATABASE_PORT", 5432)
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "api_database")
    DATABASE_URI: URL = URL.create(
        drivername="postgresql+asyncpg",
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
    )

    allowed_cors_origins: set[AnyUrl | str] = ["*"]
    allowed_cors_credentials: bool = True
    TESTING: bool = False
