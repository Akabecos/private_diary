"""
Django settings for private_diary project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_q_8qt06r7saddmf1z&n(pu%#!us&+fgmum(=6yfktf_^#x08)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "diary.apps.DiaryConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "django_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "private_diary.urls"

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

WSGI_APPLICATION = "private_diary.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "private_diary",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": "",
        "PORT": "",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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

MESSEAGES_TAGS = {
    messages.ERROR: "alert alert-danger",
    messages.WARNING: "alert alert-warning",
    messages.SUCCESS: "alert alert-success",
    messages.INFO: "alert alert-info",
}

AUTH_USER_MODEL = "accounts.CustomUser"

# django-allauthの設定
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # 一般ユーザー用(メールアドレス認証)
    "allauth.account.auth_backends.AuthenticationBackend",
    # 管理サイト用(ユーザー名認証)
    "django.contrib.auth.backends.ModelBackend",
)

# メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = False

# サインアップにメールアドレス確認を挟むように設定
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True

# ログイン、ログアウト後のリダイレクト先を設定
LOGIN_REDIRECT_URL = "diary:index"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"

# ログアウトリンクのクリック一発でログアウトする設定
ACCOUNT_LOGGOUT_ON_GET = True

# django-allauthのメール送信に関する設定
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = os.environ.get("FROM_EMAIL")
