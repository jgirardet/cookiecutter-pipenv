    # -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""
{% if cookiecutter.use_apistar == 'y' %}
# Third Party Libraries
from apistar.test import TestClient
from pseudos.models import Pseudo
import pytest

{% endif %}

# {{cookiecutter.project_name}}
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}


def test_{{cookiecutter.project_slug}}():
    assert {{cookiecutter.project_slug}}.main() == "hello"


{% if cookiecutter.use_apistar == 'y' %}

pytestmark = pytest.mark.django_db()



def test_http_request(app_fix):
    """
    Testing a view, using the test client with app_fix fixture
    """

    client = TestClient(app_fix)
    response = client.get('http://localhost/pseudos/')
    assert response.status_code == 200


def test_add_query():
    """
    Testing a db
    """
    a = Pseudo.objects.create(name="mokmok")
    b = Pseudo.objects.get(name="mokmok")

    assert a == b


def test_write():
    """
    Testing a db
    """
    a = Pseudo(name="jilj")
    a.save()
    assert a.id


def test_fixture(ss):
    a = Pseudo(name="jilj")
    a.save()
    assert ss.Pseudo.objects.get(id=a.id) == a
{% endif %}
