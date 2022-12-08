"""
Django settings for cars_world project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y!0*4-hv1ie@uuqf&q9qybr%f(%p!fm_lt%5a=dzo)05#-z!8g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']

LOGIN_URL = 'pages:login'
LOGOUT_URL = 'pages:logout'
LOGIN_REDIRECT_URL = 'pages:dashboard'

# Application definition

INSTALLED_APPS = [
    'cars.apps.CarsConfig',
    'contacts.apps.ContactsConfig',
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django.contrib.humanize',
    'social_django',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'cars_world.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here

                
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',


    
)

WSGI_APPLICATION = 'cars_world.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'carworld_db',
#        'USER' : 'postgres',
#        'PASSWORD' : 'admin',
#        'HOST' : 'localhost'
#    }
#}

DATABASES = {'default':dj_database_url.config(default = 'postgres://postgres:admin@localhost/carworld_db')}

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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'cars_world/static'),
    
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles_build','static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#sending email#
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'developervenkatesh2001@gmail.com'
EMAIL_HOST_PASSWORD = 'jhivrufehbuzajce'
EMAIL_USE_TLS = True

SOCIAL_AUTH_FACEBOOK_KEY = '912353209741051'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'fcdbf230ecfa9a34d0327ac2921fa8c0'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '101928602587-h7dhm83ikehk6258joooa9nd46ei4ot5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '866gdeoobbeday'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'aYHAei7sF8edIcoE'

#whitenoisesettings
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

cloudinary.config( 
  cloud_name = "dthrflf1k", 
  api_key = "532323486532835", 
  api_secret = "Q6CjwQko-Y4lLcOozVun71_q5rs",
  secure = True
)