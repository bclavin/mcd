"""
Django settings for mcd project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists('/Users/bclavin/sqlite/'):
    DB_DIR = '/Users/bclavin/sqlite/'
else:
    DB_DIR = '/home/ec2-user/sqlite'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i1*wd0a&x@3-!)9y^)s7b0zg2xmj32rmsxrpo72&v_%)m$$qz^'

# SECURITY WARNING: don't run with debug turned on in production!
# if os.path.exists('/Users/'):
#     DEBUG = True
# else:
#     DEBUG = False

DEBUG = True

ALLOWED_HOSTS = ['mcd-env.kpvhfrpmug.us-west-2.elasticbeanstalk.com',
                 'mycommercialdriver.golf',
                 'www.mycommercialdriver.com',
                 '127.0.0.1'
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
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

ROOT_URLCONF = 'mcd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',
                 os.path.join('homepage', 'templates'),
                 ],
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

WSGI_APPLICATION = 'mcd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if DB_DIR == '/Users/bclavin/sqlite/':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DB_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mcd',
            'USER': 'mcd',
            'PASSWORD': 'golferpw',
            'HOST': 'bclavdbs.czutsyy3pvl6.us-west-1.rds.amazonaws.com',  # Or an IP Address that your DB is hosted on
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'bclavin'
EMAIL_HOST_PASSWORD = 's3ndgr!d*8*'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'sdp <noreply@sdp.golf>'


