from sureedurecords.settings.common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'aaekb)r6%#*bz@$zfm8-4#4s-9=iiho3)af!1+9pl=+&o4(8px')

# Allowed hosts (list of comma-separated host names, or asterisk to match all hosts), only needed if DEBUG is false
ALLOWED_HOSTS = ['testserver', '*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'DEFAULT-CHARACTER-SET': 'utf8',
        # 'NAME': 'sureedurecords',
        # 'USER': 'sureedu',
        # 'PASSWORD': 'sureedu',
        # 'HOST': 'db', # OR any host for the database
        # 'PORT': 5432,
        # 'TEST': {
        #     'NAME': 'testdatabase',
        # },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    # },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
