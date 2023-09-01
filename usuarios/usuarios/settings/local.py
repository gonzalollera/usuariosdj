from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": getSecret("DB_NAME"),
        "USER": getSecret("USER"),
        "PASSWORD": getSecret("PASSWORD"),
        "HOST": getSecret("HOST"),
        "PORT" : getSecret("PORT")      
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS=[BASE_DIR.child('static')]

MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media')
