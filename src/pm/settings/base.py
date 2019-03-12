"""
Django settings for pm project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

DEBUG = None

ALLOWED_HOSTS = []

# Application definition

CUSTOM_APPS = [
    'accounts',
    'projects',
]

EXTERNAL_APPS = [
    'crispy_forms',
    'rest_framework',
    'mptt',
    'django_mptt_admin',
    'protector',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

PROTECTOR_GENERIC_GROUP = 'accounts.AccountGroup'

INTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = INTERNAL_APPS + CUSTOM_APPS + EXTERNAL_APPS

PROTECTOR_GENERIC_GROUP = 'accounts.AccountGroup'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pm.urls'

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

WSGI_APPLICATION = 'pm.wsgi.application'

# # Redis settings
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# REDIS_DB = 0
# CASHES = {
#     'redis': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': os.environ.get('CASHE_LOCATION', 'redis://127.0.0.1:6379/1'),
#         'TIMEOUT': 60,  # seconds
#         'KEY_PREFIX': os.environ.get('CASHE_KEY', 'projectManager'),
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'IGNORE_EXCEPTIONS': True,
#         }
#     }
# }
# CASHES['default'] = CASHES['redis']
# SESSION_ENGINE = 'django.contrib.session.backends.cache'
# SESSION_CACHE_ALIAS = 'default'


AUTHENTICATION_BACKENDS = [
    'accounts.backend.AccountBackend'
]
AUTH_USER_MODEL = 'accounts.Account'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'tmp')

# LOGIN_REDIRECT_URL = 'dashboard'
# LOGIN_URL = 'login'
# LOGOUT_REDIRECT_URL = 'login'

# TODO: TECHNOLOGY . WhiteNoise
#  https://github.com/evansd/whitenoise/blob/8a374b49fb4bf8e17af4d51f3bfabb3e08d783a8/docs/index.rst
# TODO: TECHNOLOGY . Bootstrap4
#  https://django-bootstrap4.readthedocs.io/en/stable/index.html
# TODO: TECHNOLOGY . xtml12pdf
# TODO: TECHNOLOGY . python-social-auth
#  https://github.com/python-social-auth/social-app-django


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'
STATICFILES_DIRS = []

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'accounts.authentication.EmailAuthBackend',
#     'social_core.backends.facebook.FacebookOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.google.GoogleOAuth2',
# ]
#
# # social auth settings
# SOCIAL_AUTH_FACEBOOK_KEY = '' # Facebook App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = '' # Facebook App Secret
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
#
# SOCIAL_AUTH_TWITTER_KEY = '' # Twitter Consumer Key
# SOCIAL_AUTH_TWITTER_SECRET = '' # Twitter Consumer Secret
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # Google Consumer Key
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # Google Consumer Secret
#
#
# from django.urls import reverse_lazy
#
# ABSOLUTE_URL_OVERRIDES = {
#     'auth.user': lambda u: reverse_lazy('user_detail',
#                                         args=[u.username])
# }
#
#
