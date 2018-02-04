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
#project has to be added before app for python path purpose
INSTALLED_APPS = [
    '{{cookiecutter.project_slug}}.pseudos',
]

SECRET_KEY = env['SECRET_KEY']

# added for manage.py only
DEBUG = env['DEBUG']
