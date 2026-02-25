import os
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy import URL
from fastapi.templating import Jinja2Templates


load_dotenv(verbose=True)


class AppSettings(BaseSettings):
    SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")

    DATABASE_USER: ClassVar[str] = os.getenv("POSTGRES_USER", "admin")
    DATABASE_PASSWORD: ClassVar[str] = os.getenv("POSTGRES_PASSWORD")
    DATABASE_HOST: ClassVar[str] = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: ClassVar[int] = os.getenv("DATABASE_PORT", 5432)
    DATABASE_NAME: ClassVar[str] = os.getenv("DATABASE_NAME", "api_database")
    DATABASE_URI: ClassVar[URL] = URL.create(
        drivername="postgresql+asyncpg",
        username=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME,
    )

    EMAIL_INVITE_TOKEN_EXPIRE_HOURS: ClassVar[int] = 72
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: ClassVar[int] = 24
    RECOVERY_EXPIRATION_DAYS: ClassVar[int] = 3

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent.parent
    templates: ClassVar[Jinja2Templates] = Jinja2Templates(directory=str(BASE_DIR / "templates"))
    DATABASE_DIR: ClassVar[Path] = BASE_DIR / "db"
    # FRONTEND_URL: ClassVar[str] = os.getenv("FRONTEND_URL")
    SECRET_KEYS_DIR: ClassVar[Path] = BASE_DIR / "core" / "auth" / "secrets"
