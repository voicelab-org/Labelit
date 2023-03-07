"""
Django settings for labelit project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
from distutils.util import strtobool

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

import os
import secrets
import string

choices = string.ascii_letters + string.digits + "<>()[]*?@!#~,.;"
key = "".join(secrets.choice(choices) for n in range(100))

SECRET_KEY = os.environ.get("SECRET_KEY", key)

import logging

logger = logging.getLogger(__name__)


def compute_django_debug_from_env_var():
    debug = os.environ.get("DJANGO_DEBUG")
    if debug and debug.lower() == "true":
        return True
    return False


DEBUG = compute_django_debug_from_env_var()

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "backend", os.environ.get("ALLOWED_HOST", "")]

# & TEMP
# APPEND_SLASH = False
# & end TEMP

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "polymorphic",
    "rest_framework",
    "corsheaders",
    "django_extensions",
    "rest_framework_simplejwt.token_blacklist",
    "users",
    "auth_api",
    "labelit.apps.labelitConfig",
]

MIDDLEWARE = [
    "labelit.middlewares.health_check_middleware.HealthCheckMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [],
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_USER_MODEL = "users.User"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Django REST Framework (DRF)

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "labelit.utils.drf_utils.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        #'rest_framework.authentication.SessionAuthentication',
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
}

SIMPLE_JWT_SIGNING_KEY = "b=72^ado*%1(v3r7rga9ch)03xr=d*f)lroz94kosf!61((9=i"


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=4),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=48),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SIMPLE_JWT_SIGNING_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]


# CSRF

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]


AWS_S3_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL")
AWS_DEFAULT_ACL = None

# HLS related params
S3_DIRECT_SERVE = strtobool(
    os.getenv("S3_DIRECT_SERVE", "true")
)  # Set to True when in the cloud, False locally.

### HACK ALERT !!
S3_DIRECT_SERVE = False
### END HACK

SEGMENT_EXPIRATION_TIME_IN_SECONDS = int(
    os.getenv("SEGMENT_EXPIRATION_TIME_IN_SECONDS", 3600)
)
NUM_ELEMENTS_IN_WAVEFORM = 1024

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "class": "coloredlogs.ColoredFormatter",
            "format": "[{levelname}:{asctime:8s}.{msecs:03.0f}] {message} [{filename}:{lineno:d},{funcName}()]",
            "style": "{",
        },
        "json": {
            "class": "labelit.log.JSONFormatter",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "console_dev": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "console_prod": {
            "level": "INFO",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "loggers": {
        "": {
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
        "django": {
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
        "botocore": {
            "level": os.getenv("BOTO3_LOG_LEVEL", "ERROR"),
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
        "boto3": {
            "level": os.getenv("BOTO3_LOG_LEVEL", "ERROR"),
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
        "s3transfer": {
            "level": os.getenv("BOTO3_LOG_LEVEL", "ERROR"),
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console_dev", "console_prod"],
            "propagate": False,
        },
    },
}
