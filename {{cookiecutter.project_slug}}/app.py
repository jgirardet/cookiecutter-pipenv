""" 
    Apistar Main App
"""

# Standard Libraries
import importlib
import os

# Third Party Libraries
import django
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App
from apistar_shell import commands as apistar_shell_commands
from apistar_shell import components as apistar_shell_components
from config.django import settings as django_settings
from django.apps import apps

# Django Must Be configured before anything in apistar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.settings')
if not apps.ready:
    django.setup()

# apistar configs, urls have to be imported AFTER django is ready
apistar_settings = importlib.import_module('config.settings')

# All routes are based on config.urls.routes
routes = importlib.import_module('config.urls').routes

# collect All components
components = [*django_orm.components, *apistar_shell_components.components]

# Merge apistar and django settings, so everything is in Settings component
# For testing and doc, this one bellow schould be imported
settings = {**apistar_settings.__dict__, **django_settings.__dict__}

# Collect all commands
commands = [*django_orm.commands, *apistar_shell_commands.django_commands]
app = App(
    routes=routes, settings=settings, commands=commands, components=components)

if __name__ == '__main__':
    app.main()