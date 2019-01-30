from sureedurecords.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aaekb)r6%#*bz@$zfm8-4#4s-9=iiho3)af!1+9pl=+&o4(8px'

# Allowed hosts (list of comma-separated host names, or asterisk to match all hosts), only needed if DEBUG is false
ALLOWED_HOSTS = ['testserver', '*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sureedurecords',
        'USER': 'sureedu',
        'PASSWORD': 'sureedu',
        'HOST': 'localhost', # OR any host for the dataase
        'PORT': 3306,
        'TEST': {
            'NAME': 'testdatabase',
        },
        'DEFAULT-CHARACTER-SET': 'utf8',
    }
}

CACHES = {
    # 'default': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': 'redis://redis:6379/',
    #     'OPTIONS': {
    #         'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    #     }
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}