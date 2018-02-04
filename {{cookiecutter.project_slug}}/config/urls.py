{% if cookiecutter.use_apistar == 'y' %}
# Third Party Libraries
from apistar import Include
from apistar.handlers import docs_urls
from apistar.handlers import static_urls
from {{cookiecutter.project_slug}}.pseudos.urls import pseudo_urls

routes = [
    Include('/docs', docs_urls),
    Include('/static', static_urls),
    Include('/pseudos', pseudo_urls),
]
{% endif %}