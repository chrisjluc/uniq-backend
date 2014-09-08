"""
Django settings for uniq project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd(tl*aopb!^(1ge0yu-x5+tmbd(h*6x(58ig84j39a_8@2dt88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (('Chris', 'chris.luc93@gmail.com'), ('Si te', 'fengsite@hotmail.com'))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'schools',
    'faculties',
    'programs',
    'uniqdata',
    'explore',
    'featured',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uniq.urls'

WSGI_APPLICATION = 'uniq.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

# Application Constants / Settings
CURRENT_YEAR = 2015
MAX_FEATURED = 10

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

TEST_RUNNER = (
    'uniq.testing.testrunners.MongoTestRunner'
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

# Mongo Database Connection

MONGO_DATABASE_NAME = 'uniq_db'
MONGO_HOST = '54.85.16.143'
MONGO_PORT = 27017

#1 day
CACHE_MAX_EXPIRY=86400

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'default',
            'MAX_ENTRIES': 100
        }
    },
    'school': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'school',
            'MAX_ENTRIES': 20
        }
    },
    'faculty': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'faculty',
            'MAX_ENTRIES': 20
        }       
    },
    'program': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'program',
            'MAX_ENTRIES': 20
        }
    },
    'school_explore': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'school_explore',
            'MAX_ENTRIES': 20
        }
    },
    'faculty_explore': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'faculty_explore',
            'MAX_ENTRIES': 20
        }
    },
    'program_explore': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': CACHE_MAX_EXPIRY,
        'OPTIONS': {
            'KEY_PREFIX': 'program_explore',
            'MAX_ENTRIES': 20
        }
    }
}

from mongoengine import *
import sys

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
    MONGO_DATABASE_NAME = 'uniq_test_db'

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'school': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'faculty': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'program': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'school_explore': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'faculty_explore': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
       'program_explore': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

from uniqdb import UniqDb
from uniqdata.datainitializer import DataInitializer
import logging

logging.basicConfig()

db = UniqDb()
db.clearCollections()

di = DataInitializer()
di.run()