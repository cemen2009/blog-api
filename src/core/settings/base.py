import os
from enum import StrEnum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv(verbose=True)


class AppEnvTypes(StrEnum):
    development = "development"
    production = "production"
    qa = "qa"


class AppUploadFolders(StrEnum):
    users = "users"


class BaseAppSettings(BaseSettings):
    ENV: AppEnvTypes = os.getenv("ENV") or AppEnvTypes.development
