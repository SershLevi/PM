from .base import *

DEBUG = False

DATABASES = {
    'default': {
    }
}

SECRET_KEY = '32v6y@dq4n#gzzal(36^fs8^7e3hqx*5u1)u2p5#=h-oz&#(-)' #TODO: Удалить

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'max_similarity': 0.5,
        },

    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        },

    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'pm.auth_extra.SpecialCharactersInclusionValidator',
    },
]
