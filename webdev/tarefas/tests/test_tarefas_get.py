import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixture
def response(client):
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(response):
    assert response.status_code == 200

def test_formulario_presente(response):
    assertContains(response, '<form')

def test_botao_salvar_presente(response):
    assertContains(response, '<button type="submit"')