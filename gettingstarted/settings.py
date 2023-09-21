"""
Django settings for gettingstarted project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import environ
import os, boto3
import secrets
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from storages.backends.s3boto3 import S3Boto3Storage


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ENVIRON PATH
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Before using your Heroku app in production, make sure to review Django's deployment checklist:
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Django requires a unique secret key for each Django app, that is used by several of its
# security features. To simplify initial setup (without hardcoding the secret in the source
# code) we set this to a random value every time the app starts. However, this will mean many
# Django features break whenever an app restarts (for example, sessions will be logged out).
# In your production Heroku apps you should set the `DJANGO_SECRET_KEY` config var explicitly.
# Make sure to use a long unique value, like you would for a password. See:
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY
# https://devcenter.heroku.com/articles/config-vars
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(nbytes=64),
)
# print(SECRET_KEY)

# The `DYNO` env var is set on Heroku CI, but it's not a real Heroku app, so we have to
# also explicitly exclude CI:
# https://devcenter.heroku.com/articles/heroku-ci#immutable-environment-variables
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU_APP:
    DEBUG = True

# On Heroku, it's safe to use a wildcard for `ALLOWED_HOSTS``, since the Heroku router performs
# validation of the Host header in the incoming HTTP request. On other platforms you may need
# to list the expected hostnames explicitly to prevent HTTP Host header attacks. See:
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-ALLOWED_HOSTS
if IS_HEROKU_APP:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Use WhiteNoise's runserver implementation instead of the Django default, for dev-prod parity.
    "whitenoise.runserver_nostatic",
    # Uncomment this and the entry in `urls.py` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # USER APPS
    "hello",
    "accounts",

    # THIRD_PARTY_APPS
    'rosetta',
    'storages',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Django doesn't support serving static assets in a production-ready way, so we use the
    # excellent WhiteNoise package to do so instead. The WhiteNoise middleware must be listed
    # after Django's `SecurityMiddleware` so that security redirects are still performed.
    # See: https://whitenoise.readthedocs.io
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = [
    'accounts.authentication.CustomUserModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = "gettingstarted.urls"
# LOGIN URL
LOGIN_URL = '/accounts/login/'
AUTH_USER_MODEL = 'accounts.User'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
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

WSGI_APPLICATION = "gettingstarted.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env('AWS_DB_NAME'),
            "USER": env('AWS_DB_USER'),
            "PASSWORD": '8123ca82a28b07f2e08a6428916a9ebd7d9129d328f3ca5769bf815f33a27008',
            "HOST": env('AWS_DB_HOST'),
            "PORT": 5432,
        }
    }

else:
    # When running locally in development or in CI, a sqlite database file will be used instead
    # to simplify initial setup. Longer term it's recommended to use Postgres locally too.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
LANGUAGES = [
    ('en', _('English')),
    ('km', _('Khmer')),  # Khmer
]
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
DATE_INPUT_FORMATS = ['%d-%m-%Y']




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Use AWS S3 storage for static and media files on Heroku
# Static and Media settings
if IS_HEROKU_APP:
    # AWS S3 configuration
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'bucketeer-8c8c929a-3664-4540-b0b0-c7ea9765fbb3'
    AWS_DEFAULT_REGION = 'us-east-1'  # Region
    # AWS_DEFAULT_ACL = None
    AWS_S3_ENDPOINT_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_SIGNATURE_VERSION = env('S3_SIGNATURE_VERSION', default='s3v4')
    PUBLIC_URL = 'https://bucketeer-8c8c929a-3664-4540-b0b0-c7ea9765fbb3.s3.amazonaws.com/public/'
    

    # # Use S3 for static files storage
    STORAGES = {
        'default': {
            'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
            'LOCATION': 'media',
             'OPTIONS': {
                'access_key': 'AKIAVVKH7VVUMTNQINWO',
                'secret_key': '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',
                'bucket_name': 'bucketeer-8c8c929a-3664-4540-b0b0-c7ea9765fbb3',
                'region_name': 'us-east-1',
                'gzip': True,
                'use_ssl': True,
                'querystring_expire':86400,
                'querystring_auth': False,
                'gzip_content_types': ('text/css','text/javascript','application/javascript','application/x-javascript','image/svg+xml'),
                'signature_version': 's3v4', 
             },
        },
        
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            'LOCATION': 'static',
            'OPTIONS': {
                'access_key': 'AKIAVVKH7VVUMTNQINWO',
                'secret_key': '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',
                'bucket_name': 'bucketeer-8c8c929a-3664-4540-b0b0-c7ea9765fbb3',
                'region_name': 'us-east-1',
                'gzip': True,
                'use_ssl': True,
                'querystring_expire':86400,
                'querystring_auth': False,
                'gzip_content_types': ('text/css','text/javascript','application/javascript','application/x-javascript','image/svg+xml'),
                'signature_version': 's3v4', 
             },
        },     
    }
  
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}public/media/'
    STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}public/static/' 
    
   
    
else:
    STORAGES = {
        'default': {
            'BACKEND': 'django.core.files.storage.FileSystemStorage',
            'LOCATION': [
                os.path.join(BASE_DIR, 'media'), 
                os.path.join(BASE_DIR, 'static')
                         
            ],
        },
        "staticfiles": {
            # Enable WhiteNoise's GZip and Brotli compression of static assets:
            # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    # Use WhiteNoise for development environment
    STATIC_URL = "static/"
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   

    # Media files
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # STATICFILES_DIRS = [
    #     os.path.join(BASE_DIR, 'staticfiles'),
    # ]
    WHITENOISE_KEEP_ONLY_HASHED_FILES = True
   

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Other settings...
# Use FileSystemStorage for development environment
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# Enable WhiteNoise's GZip and Brotli compression of static assets
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Don't store the original (un-hashed filename) version of static files, to reduce slug size:
# https://whitenoise.readthedocs.io/en/latest/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

