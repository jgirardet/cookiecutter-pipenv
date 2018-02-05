# Standard Libraries
import pathlib
import sys

# Third Party Libraries
from apistar import environment
from apistar import typesystem


class Env(environment.Environment):
    properties = {
        'DB_ENGINE': typesystem.string(default='django.db.backends.sqlite3'),
        'DB_PORT': typesystem.string(default=''),
        'DB_NAME': typesystem.string(default='db.local'),
        'DB_HOST': typesystem.string(default=''),
        'DB_USER': typesystem.string(default=''),
        'DB_PASSWORD': typesystem.string(default=''),
        'SECRET_KEY': typesystem.string(default='please_change_it'),
        'DEBUG': typesystem.boolean(default=True),
    }


env = Env()

# add app folder to sys.path when imported in app.py
PROJECT_ROOT = pathlib.Path(__file__).absolute()
PROJECT_ROOT = PROJECT_ROOT.parents[2] / "{{cookiecutter.project_slug}}"
sys.path.insert(0, str(PROJECT_ROOT))
