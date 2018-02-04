from apistar import environment
from apistar import typesystem
import pathlib
import sys


class Env(environment.Environment):
    properties = {
        'DB_ENGINE':
        typesystem.string(default='django.db.backends.sqlite3'),
        'DB_PORT':
        typesystem.string(default=''),
        'DB_NAME':
        typesystem.string(default=':memory:'),
        'DB_HOST':
        typesystem.string(default=''),
        'DB_USER':
        typesystem.string(default=''),
        'DB_PASSWORD':
        typesystem.string(default=''),
        'SECRET_KEY':
        typesystem.string(default=''),
        'DJANGO_SETTINGS_MODULE':
        typesystem.string(default='config.base_settings'),
        'DEBUG':
        typesystem.boolean(default=False),
    }


env = Env()

# add app folder to sys.path when imported in app.py
PROJECT_ROOT = pathlib.Path(__file__).absolute()
PROJECT_ROOT = PROJECT_ROOT.parents[1] / "{{cookiecutter.project_slug}}"
sys.path.insert(0, str(PROJECT_ROOT))
