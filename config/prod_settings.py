import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(isdfwetyr435346w!lr%g^i7qx%!rghe#g53_m7ff567567frgf'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "128.199.54.39"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'course',
        'USER': 'john',
        'PASSWORD': 'Q1W2e3r4T5',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'email'
EMAIL_HOST = 'smtp'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
