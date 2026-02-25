import os
from functools import lru_cache
from typing import Type

from dotenv import load_dotenv

from settings import AppEnvTypes, DevelopmentSettings, AppSettings


settings_per_environment: dict = {
    AppEnvTypes.development: DevelopmentSettings,
}


@lru_cache
def get_settings() -> Type[AppSettings]:
    load_dotenv(verbose=True)

    env: AppEnvTypes = os.getenv("ENV") # type: ignore
    config = settings_per_environment.get(env)

    if not env:
        raise ValueError(f"ENV value is empty")
    elif config is None:
        raise ValueError(f"ENV value '{env}' doesn't exist\nExisting and implemented values: {[env.value for env in settings_per_environment.keys()]}")

    return config
