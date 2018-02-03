#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""

# Third Party Libraries
from apistar.test import TestClient
from app import app

# Third Party Libraries
import pytest

# {{cookiecutter.project_name}}
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}
from {{cookiecutter.project_slug}}.pseudo.models import Pseudo

def test_{{cookiecutter.project_slug}}():
    assert True


def test_pseudo():
    assert Pseudo.name == "pseudo"



{% if cookiecutter.use_apistar == 'y' %}

def test_http_request():
    """
    Testing a view, using the test client with
    """
    client = TestClient(app)
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200

{% endif %}

{% if cookiecutter.use_django_with_apistar == 'y' %}
def test_http_request(ss):
    """
    Testing a view, using the test client with
    but testing with fixture
    """
    client = TestClient(app)
    e = ss.Pseudo.objects.all()
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200
{% endif %}