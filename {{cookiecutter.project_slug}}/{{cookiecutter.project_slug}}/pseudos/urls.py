# Third Party Libraries
from apistar import Route

from .views import get_pseudos, pseudo_create

pseudo_urls = [
    Route('/', 'POST', pseudo_create),
    Route('/', 'GET', get_pseudos),
]
