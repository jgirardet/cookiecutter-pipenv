    # -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""
{% if cookiecutter.use_apistar == 'y' %}
# Third Party Libraries
from apistar.test import TestClient
from app import app
from pseudos.models import Pseudo

{% endif %}

# {{cookiecutter.project_name}}
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}

def test_{{cookiecutter.project_slug}}():
    assert {{cookiecutter.project_slug}}.main() == "hello"


{% if cookiecutter.use_apistar == 'y' %}

def test_http_request():
    """
    Testing a view, using the test client with
    """
    client = TestClient(app)
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200

def test_http_request_with_fixture(ss):
    """
    Testing a view, using the test client with
    but testing with fixture
    """
    client = TestClient(app)
    e = ss.Pseudo.objects.all()
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200
{% endif %}