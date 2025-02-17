"""
Django settings for synth_invo_analyzer project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--^j063vts8lgc2(a$%96!(!$%#-mp1#x_$4wz8ls^f9_3vy9zx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'rest_framework',
    'channels',
    'django_cassandra_engine',
    'django_elasticsearch_dsl',
    'corsheaders',
    'authentication',
    'invoice_template',
    'invoice',
    'subscription_models',
    'subscriptions',
    'invoice_analysis',
    'search',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'synth_invo_analyzer.urls'

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

WSGI_APPLICATION = 'synth_invo_analyzer.wsgi.application'

ASGI_APPLICATION = 'synth_invo_analyzer.asgi.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
     'cassandra': {
         'ENGINE': 'django_cassandra_engine',
         'NAME': 'synth_invo_analyzer',
         'TEST_NAME': '',
         'HOST': '3.109.239.176',
         'OPTIONS': {
             'replication': {
                 'strategy_class': 'SimpleStrategy',
                 'replication_factor': 3
             }
         }
     },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'synth_invo_analyzer',
        'USER': 'Asela',
        'PASSWORD': 'Aa@12345',
        'HOST': 'synthinvoanalyzer.mysql.database.azure.com',
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Colombo'
USE_TZ = True 

USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}







AUTH_USER_MODEL = 'authentication.User'

AUTHENTICATION_BACKENDS = [
    'authentication.backends.CustomUserAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]



CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'Access-Control-Allow-Origin',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'synthinvoanalyzer@gmail.com'
EMAIL_HOST_PASSWORD = 'ohpb xyoh nqrt ojai '


ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://43.204.122.107:9200'
    },
}



