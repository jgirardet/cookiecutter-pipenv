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

django.setup()

from config.urls import routes

if get_env.env['DEBUG']:
    from config import local_settings as settings
else:
    from config import prod_settings as settings

app = App(
    routes=routes,
    settings=settings.__dict__,
    commands=django_orm.commands,  # Install custom commands.
    components=django_orm.components,  # Install custom components.
)

if __name__ == '__main__':
    app.main()
