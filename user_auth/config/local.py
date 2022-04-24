from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

CORS_ALLOW_ALL_ORIGINS = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     env.str('MYSQL_DATABASE'),
        'USER':     env.str('MYSQL_USER'),
        'PASSWORD': env.str('MYSQL_PASSWORD'),
        'HOST':     env.str('MYSQL_HOST'),
        'PORT':     env.int('MYSQL_PORT'),
    }
}

