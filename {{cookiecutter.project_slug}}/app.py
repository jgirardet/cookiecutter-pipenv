""" 
    Apistar Main App
"""

# Standard Libraries
import importlib

# Third Party Libraries
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App
#setting check various env issues
from config import settings

# manual import of routes to prevent automatic sorting, be sure this is AFTER django_setup in settings
routes = importlib.import_module('config.urls').routes

components = []
components = components + django_orm.components  #add the others components with +

app = App(
    routes=routes,
    settings=settings.__dict__,
    commands=django_orm.commands,  # Install custom commands.
    components=components  # Install custom components.
)

if __name__ == '__main__':
    app.main()
