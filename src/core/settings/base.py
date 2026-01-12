import os
from enum import StrEnum

from pydantic_settings import BaseSettings


class AppEnvTypes(StrEnum):
    development = "development"


class AppUploadFolders(StrEnum):
    users = "users"


class BaseAppSettings(BaseSettings):
    env: AppEnvTypes = os.getenv("ENV") or AppEnvTypes.development
