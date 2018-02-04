""" 
    Apistar Main App
    trouble with django, pytest, configure...

    routes has to be imported AFTER django_setup()

   isort:skip_file
"""

import django
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App
from config import get_env
import importlib

# to make apistar, pytest and django happy togther
# django.setup() must be run before routes because route immports Model a the end and django_setup must be run before
django.setup()
# manual import of routes to prevent automatic sorting, be sure this is AFTER django_setup
routes = importlib.import_module('config.urls').routes
# give the good settings depending environ modified in .env or pytest
django_settings = importlib.import_module(
    get_env.env['DJANGO_SETTINGS_MODULE'])

app = App(
    routes=routes,
    settings=django_settings.__dict__,
    commands=django_orm.commands,  # Install custom commands.
    components=django_orm.components,  # Install custom components.
)

if __name__ == '__main__':
    app.main()
