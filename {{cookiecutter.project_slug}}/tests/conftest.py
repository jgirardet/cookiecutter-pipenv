# -*- coding: utf-8 -*-

import typing
from contextlib import contextmanager

import pytest

from apistar import Component
from apistar.backends.django_orm import DjangoORM
from apistar.backends.django_orm import Session
from apistar.frameworks.wsgi import WSGIApp as App
from app import components
from config import settings
from config.urls import routes


@pytest.fixture(autouse=True)
def ss(db):
    """
    session from django backend
    may be passed as parameter for testing views with session as argument
    """

    return Session(DjangoORM(settings.__dict__))


@contextmanager
def get_ss(backend: DjangoORM) -> typing.Generator[Session, None, None]:
    """
    Just a copy of django_orm.get_session but without all database related thing
    """
    yield Session(backend)


@pytest.fixture(autouse=True)
def app_fix():
    """
    fixture for apistar app
    Juste mock get_session to get_ss
    Use all regular routes and componements of app.py
    """
    comp = []
    for c in components:
        if c.cls is Session:
            c = Component(Session, init=get_ss, preload=False)
        comp.append(c)
    return App(routes=routes, settings=settings.__dict__, components=comp)

    return Session(DjangoORM(settings.__dict__))
