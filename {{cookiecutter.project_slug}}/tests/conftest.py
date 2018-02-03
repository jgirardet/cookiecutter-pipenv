# Third Party Libraries
import pytest
from apistar.backends.django_orm import DjangoORM
from apistar.backends.django_orm import get_session
from config import test_settings


@pytest.fixture(autouse=True)
def ss(db):
    """
    session from django backend
    may be passed as parameter for testing views with session as argument
    """
    with get_session(DjangoORM(test_settings.__dict__)) as s:
        yield s
