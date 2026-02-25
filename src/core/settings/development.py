import logging
from typing import ClassVar

from dotenv import load_dotenv

from core.settings import AppSettings


load_dotenv(verbose=True)


class DevelopmentSettings(AppSettings):
    DEBUG: ClassVar[bool] = True
    LOGGING_LEVEL: ClassVar[int] = logging.DEBUG

    ACCESS_TOKEN_EXPIRATION_MINUTES: ClassVar[int] = 76 * 60
    INVITE_EXPIRATION_MINUTES: ClassVar[int] = 24 * 60

    SMTP_TIMEOUT: ClassVar[int] = 10    # seconds (if you expect not seconds, you are pretty bum)
