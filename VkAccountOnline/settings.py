"""
Django settings for VkAccountOnline project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+j4r#7_=6(@7l8%lmm16em^zm4%%56f)%i^$*3^nzb^t=a-4o!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'django_filters',
    'debug_toolbar',
    'app_vk_controller.apps.AppVkControllerConfig',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VkAccountOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'VkAccountOnline.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     'LOCATION': Path(BASE_DIR, 'django_cache'),
    # 'TIMEOUT': 10800
    # },
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.redis.RedisCache',
    #     'LOCATION': 'redis://127.0.0.1:6379',
    # }

    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'TIMEOUT': 60 * 60 * 1
    # }
}

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        # 'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        # 'NAME': os.environ.get('POSTGRES_NAME'),
        # 'USER': os.environ.get('POSTGRES_USER'),
        # 'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} [{asctime}] [{module}] > {message} ({process:d} {thread:d})',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/logs/main.log',
            "encoding": "utf-8",
            'formatter': 'verbose'
        },
        'file_controller': {
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/controller.log',
            "encoding": "utf-8",
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',

    },
    'controller': {
        'handlers': ['file_controller'],
        'level': 'DEBUG'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,



    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # 'rest_framework.permissions.AllowAny'
    # ]
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR, 'static')
STATICFILES_DIRS = [
    Path(BASE_DIR, 'app_vk_controller/static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
# CELERY_TASK_TRACK_STARTED = True
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'default'
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
INTERNAL_IPS = [
    '127.0.0.1',
]
