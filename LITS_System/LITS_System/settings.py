"""
Django settings for LITS_System project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'application/templates')
STATIC_DIR = os.path.join(BASE_DIR, 'application/static')
MEDIA_DIR = os.path.join(BASE_DIR, 'application/media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# SESSIONS Conflicting on password reset
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 10 # set just 10 seconds to test
# SESSION_SAVE_EVERY_REQUEST = True


# Application definition

INSTALLED_APPS = [
    'application',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'import_export',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LITS_System.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'LITS_System.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# for pthon anywhere 
# https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'lits$lits_general_system_db',
#         # username when creating access from python anywhere
#         'USER': 'lits',
#         'PASSWORD': 'r00t@passw0rd77',
#         'HOST': 'lits.mysql.pythonanywhere-services.com',
#         'PORT': '3306',
#         'OPTIONS': {
#            'init_command': 'SET default_storage_engine=INNODB',
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }
PASSWORD = os.getenv('PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lits_general_system_db',
        'USER': 'root',
        'PASSWORD': PASSWORD,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'lits_system_db',
#         'USER': 'root',
#         'PASSWORD': 'r00t@passw0rd77',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]



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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

DATETIME_FORMAT = '%b %d %Y %a %I:%M %p'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

# -------Using Gmail
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'webby8818@gmail.com'
# EMAIL_HOST_PASSWORD = 'Jh7*Mb4$Hj6#'
# # EMAIL_HOST_USER = 'lloydgarcia77@gmail.com'
# # EMAIL_HOST_PASSWORD = 'LloydQueen77'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_FROM = EMAIL_HOST_USER
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# --------Send Grid
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY') 
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
# DEFAULT_FROM_EMAIL = 'lloydgarcia77@gmail.com'
# EMAIL_FROM = 'lloydgarcia77@gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Go Daddy
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'info@lits.com.ph'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = '@Helios2o18'
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
# from cryptography.fernet import Fernet
# Fernet.generate_key()
ENCRYPT_KEY = b'xlNVkz4loCnsQWGmKEMjj7De5fj0d_N0_yeKxGJxDSk='
