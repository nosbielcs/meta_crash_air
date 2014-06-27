"""
Django settings for app2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#begin Insert Django suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + ('django.core.context_processors.request',)

#Configuration of the SUIT

SUIT_CONFIG = {
    'ADMIN_NAME': 'SIPAERSIG',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': False,
    'LIST_PER_PAGE': 100,
    'HEADER_DATE_FORMAT': 'l, j. F Y', # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',       # 18:42
    'MENU_ICONS': {
        'sipaer': 'icon-leaf',
        'auth': 'icon-lock',
    }
}

#end Django suit import

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gk19j1!@_i8p@b39%c0c65=z!z7m+$734==#xa-_0uvk*an8a@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = (
    #'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artigos',
    'sipaer',
    'treinamento',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app2.urls'

WSGI_APPLICATION = 'app2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
'''
CREATE SCHEMA IF NOT EXISTS `django` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
USE `django` ;
'''

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

LOCAL = False

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'artigos/templates')
    #'C:/wamp/www/curso_django/app2/templates',
    #'C:/wamp/www/curso_django/app2/artigos/templates',
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'meuemail@gmail.com'
EMAIL_HOST_PASSWORD = '34t56'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

