from sureedurecords.settings.common import *

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


DEBUG = config['DEBUG']

SECRET_KEY = config['SECRET_KEY']

# Allowed hosts (list of comma-separated host names, or asterisk to match all hosts), only needed if DEBUG is false
ALLOWED_HOSTS = ['testserver', '*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'DEFAULT-CHARACTER-SET': 'utf8',
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASS'],
        'HOST': config['DB_HOST'], # OR any host for the database
        'PORT': 5432,
        'TEST': {
            'NAME': 'testdatabase',
        },
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

BUGSNAG = {
    'api_key': config['BUGSNAG_API_KEY'],
    'project_root': '/code/src'
}