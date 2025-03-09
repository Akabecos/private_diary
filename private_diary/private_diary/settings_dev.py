from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_q_8qt06r7saddmf1z&n(pu%#!us&+fgmum(=6yfktf_^#x08)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    "loggers": {
        # django が利用するロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "diary": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
    "formatters": {
        "dev": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            )
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
