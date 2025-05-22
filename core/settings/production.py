import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa


###################################################################
# General
###################################################################

DEBUG = False

###################################################################
# Django security
###################################################################

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://example.com"]

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

REDIS_HOST = env.str("REDIS_HOST", "redis")
REDIS_PORT = env.int("REDIS_PORT", 6379)
REDIS_DB = env.int("REDIS_DB", 0)


sentry_sdk.init(
    dsn="some sentry dsn",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)