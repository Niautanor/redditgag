"""
Django settings for redditgag project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# django.middleware.security.SecurityMiddleware settings
# those were basically obtained by running `python manage.py check --deploy` and
# setting all the values it complained about.
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Application definition

INSTALLED_APPS = [
    'app.apps.AppConfig',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'static_precompiler',
    'djangobower',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
    'djangobower.finders.BowerFinder',
]

# For Django-bower
BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap',
    'handlebars',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'redditgag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

WSGI_APPLICATION = 'redditgag.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# redditgag/secret.py defines options that differ between development and
# production environments. An example (that you can copy / symlink to the right
# place) is given in secret_example.py
from .secret import (
        SECRET_KEY,
        DEBUG,
        ALLOWED_HOSTS,
        SECURE_SSL_REDIRECT,
        STATIC_ROOT,
        STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# this project uses Coffee script and Handlebars and only needs those compilers.
# If this setting is left at the default, static_precomipler tries to compile
# less files from bowers version of bootstrap (bower shouldn't even download
# those files but that is another issue)
STATIC_PRECOMPILER_COMPILERS = (
    'static_precompiler.compilers.CoffeeScript',
    'static_precompiler.compilers.Handlebars',
)

# collect compiled files (with collectstatic) only if we can't compile them on
# the fly (in that case it is assumed that we have run compilestatic before
# collectstatic)
STATIC_PRECOMPILER_FINDER_LIST_FILES = STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE

# django-static-precompiler will compile to this directory
STATIC_PRECOMPILER_ROOT = os.path.join(BASE_DIR, 'static_precompiler')
