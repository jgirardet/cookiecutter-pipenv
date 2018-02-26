# Third Party Libraries
from config.get_env import env

DATABASES = {
    'default': {
        'ENGINE': env['DB_ENGINE'],
        'PORT': env['DB_PORT'],
        'NAME': env['DB_NAME'],
        'HOST': env['DB_HOST'],
        'USER': env['DB_USER'],
        'PASSWORD': env['DB_PASSWORD'],
    }
}

SECRET_KEY = env['SECRET_KEY']

DJANGO_APPS = [
    # 'django.contrib.auth',  #Uncomment for to user django user model
    # 'django.contrib.contenttypes',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    'pseudos',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# change default user
# AUTH_USER_MODEL = 'users.User'

USE_TZ = True

TIME_ZONE = "Europe/Paris"