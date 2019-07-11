# -*- coding: utf-8 -*-
"""Endpoint tests."""
from django.template.response import TemplateResponse


def test_json_response(client):
    response = client.get('/versions/', **{'HTTP_ACCEPT': 'application/json'})
    assert response.status_code == 200
    result = response.json()
    assert set(result.keys()) == {'host', 'versions'}
    version_keys = set(result['versions'].keys())
    assert version_keys == {'django-version-endpoint', 'Django'}


def test_html_response(client):
    response = client.get('/versions/', **{'HTTP_ACCEPT': 'text/html'})
    assert response.status_code == 200
    assert isinstance(response, TemplateResponse)
    assert response.content == b'SUCCESS\n'


def test_default_representation(client):
    response = client.get('/versions/', **{'HTTP_ACCEPT': 'image/webp'})
    assert response.status_code == 200
    assert isinstance(response, TemplateResponse)
    assert response.content == b'SUCCESS\n'


def test_single_json_response(client):
    response = client.get(
        '/versions/django-version-endpoint/',
        **{'HTTP_ACCEPT': 'application/json'}
    )
    assert response.status_code == 200
    result = response.json()
    assert set(result.keys()) == {'version'}


def test_single_html_response(client):
    response = client.get(
        '/versions/django-version-endpoint/',
        **{'HTTP_ACCEPT': 'text/html'}
    )
    assert response.status_code == 200
    assert isinstance(response, TemplateResponse)
    assert response.content == b'SINGLE SUCCESS\n'


def test_single_forbidden_response(client):
    response = client.get(
        '/versions/pip/',
        **{'HTTP_ACCEPT': 'text/html'}
    )
    assert response.status_code == 403
