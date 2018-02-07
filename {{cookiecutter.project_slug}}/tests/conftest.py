# Third Party Libraries
import pytest
from apistar.backends.django_orm import DjangoORM, Session
from config import settings


@pytest.fixture(autouse=True)
def ss(db):
    """
    session from django backend
    may be passed as parameter for testing views with session as argument
    """
    return Session(DjangoORM(settings.__dict__))