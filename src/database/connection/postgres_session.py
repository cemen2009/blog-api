import os
from urllib.parse import quote_plus
import ssl

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


load_dotenv(verbose=True)

USER = quote_plus(os.getenv("POSTGRES_USER", "admin"))
PASSWORD = quote_plus(os.getenv("POSTGRES_PASSWORD", "password123"))
HOST = os.getenv("POSTGRES_HOST", "postgres")   # name of the service in docker-compose or name of service in k8s
NAME = os.getenv("POSTGRES_HOST", "blog_db")
PORT = os.getenv("POSTGRES_PORT", "5432")
DRIVER = "postgresql+asyncpg"

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# TODO: configure ssl context (if using AWS)
def get_ssl_context() -> ssl.SSLContext | None:
    ...

ssl_context = get_ssl_context()
connect_args = {"ssl": ssl_context} if ssl_context else {}

POSTGRES_DATABASE_URL = f"{DRIVER}//{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
postgres_engine = create_async_engine(
    POSTGRES_DATABASE_URL,
    echo=True,  # what does it mean?
    future=True,
    connect_args=connect_args,  # what does it mean?
    pool_pre_ping=True, # what does it mean?
    pool_size=3600, # what does it mean?
)
