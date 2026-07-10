import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")


# Insecure placeholder so the project runs out of the box for local development
# and tests. Always set a real SECRET_KEY via the environment in production.
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-local-dev-key")

DEBUG = env_bool("DEBUG", False)

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "tokens",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SWAGGER_USE_COMPAT_RENDERERS = False

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.SessionAuthentication",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 200,
    "MAX_PAGE_SIZE": 500,
}

ROOT_URLCONF = "nft_generator.urls"

WSGI_APPLICATION = "nft_generator.wsgi.application"

# Defaults to a local SQLite file so the project runs with zero setup.
# Set DB_ENGINE to django.db.backends.postgresql (see .env.example)
# to use Postgres, as the Docker setup does.
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

INFURA_URL = os.environ.get("INFURA_URL")
# Public address of the demo ERC-721 contract on Sepolia; not sensitive data.
CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS", "0x399c1448e0F34aB3722e3aFDd21301Ca6cFF4c4a")
# The ABI is public, static contract metadata, not a per-environment secret, so it lives in a
# version-controlled file. CONTRACT_ABI env var, if set, overrides it (e.g. for a different
# contract than the bundled demo one).
CONTRACT_ABI_PATH = BASE_DIR / "tokens" / "contract_abi.json"
CONTRACT_ABI = json.loads(os.environ.get("CONTRACT_ABI") or CONTRACT_ABI_PATH.read_text())
PUBLIC_ADDRESS = os.environ.get("PUBLIC_ADDRESS")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Sepolia testnet. Override for a different network.
CHAIN_ID = int(os.environ.get("CHAIN_ID", "11155111"))
GAS_LIMIT = int(os.environ.get("GAS_LIMIT", "300000"))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS: list[str] = []
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
