# Third Party Libraries
from apistar import environment
from apistar import typesystem
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App
# from config import base_settings
from config.urls import routes


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=False),
    }


env = Env()

routes = routes

if env['DEBUG']:
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
