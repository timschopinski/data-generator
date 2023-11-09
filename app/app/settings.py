"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s5=sy*3-7%qa7-#rqtn0*_fk9%*v4ug7&v#2r@#m_*j@zl1qwr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MYSQL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if MYSQL:
    DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'carshare',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import logging
from colorlog import ColoredFormatter

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'colored': {
            '()': ColoredFormatter,
            'format': '%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s',
            'log_colors': {
                'DEBUG': 'reset',
                'INFO': 'reset',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            },
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

manufacturer_models = {
    'BMW': {
        'models': ['M5', 'X6', 'M2', 'X1'],
        'types': ['Sedan', 'SUV', 'Coupe', 'SUV'],
    },
    'Audi': {
        'models': ['A4', 'Q5', 'S3', 'Q3'],
        'types': ['Sedan', 'SUV', 'Sedan', 'SUV'],
    },
    'Volkswagen': {
        'models': ['Golf', 'Passat', 'Tiguan', 'Jetta'],
        'types': ['Hatchback', 'Sedan', 'SUV', 'Sedan'],
    },
    'Ford': {
        'models': ['Mustang', 'Explorer', 'Escape', 'Focus'],
        'types': ['Coupe', 'SUV', 'SUV', 'Hatchback'],
    },
    'Mercedes': {
        'models': ['C-Class', 'E-Class', 'GLC', 'S-Class'],
        'types': ['Sedan', 'Sedan', 'SUV', 'Sedan'],
    },
}


BACKUP_DIR = BASE_DIR / 'data' / 'backups'

CSV_COLUMNS = [
    "Numer rejestracyjny",
    "Przebieg",
    "Poziom oleju",
    "Poziom płynu chłodniczego",
    "Poziom płynu hamulcowego",
    "Poziom płynu do spryskiwaczy",
    "Stan wizualny",
    "Stan techniczny"
]

CSV_FILE_NAME = "stan_techniczny_samochodow.xlsx"