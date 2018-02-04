# Standard Libraries
import pathlib
import sys

from .get_env import env

# add app folder to sys.path
PROJECT_ROOT = pathlib.Path(__file__).absolute()
PROJECT_ROOT = PROJECT_ROOT.parents[1] / "{{cookiecutter.project_slug}}"
sys.path.insert(0, str(PROJECT_ROOT))

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
    'pseudos',
]

SECRET_KEY = env['SECRET_KEY']

# added for manage.py only
DEBUG = env['DEBUG']
