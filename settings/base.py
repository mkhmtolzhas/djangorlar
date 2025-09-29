import os

from settings.conf import *  # noqa

# ----------------------------------------------------------------
# Path
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
WSGI_APPLICATION = "settings.wsgi.application"
ROOT_URLCONF = "settings.urls"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ----------------------------------------------------------------
# Apps
#
DJANGO_AND_THIRD_PARTY_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.welcome",
    "apps.users",
]
INSTALLED_APPS = PROJECT_APPS + DJANGO_AND_THIRD_PARTY_APPS


# ----------------------------------------------------------------
# Middleware | Templates | Validators
#
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
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


# ----------------------------------------------------------------
# Internationalization
#

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


SECRET_KEY = "django-insecure-bqt7^m_m908t-xnc6!gh(bn&indw#)9sr!@3m&(#yn*_-sz03c"
