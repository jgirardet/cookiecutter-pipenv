from .get_env import env

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

INSTALLED_APPS = [
    'pseudos',
]

SECRET_KEY = env['SECRET_KEY']

# added for manage.py only
DEBUG = env['DEBUG']
