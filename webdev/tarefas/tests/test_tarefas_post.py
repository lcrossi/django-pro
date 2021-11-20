import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa


@pytest.fixture
def response(client, db): #a operação envolve o banco de dados
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp

def test_tarefa_existe_no_db(response):
    assert Tarefa.objects.exists()

def test_redirecionamento_depois_do_salvamento(response):
    assert response.status_code == 302 #verifica se o status code dá página é o de direcionamento

@pytest.fixture
def response_dado_invalido(client, db): #a operação envolve o banco de dados
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp

def test_tarefa_nao_existe_no_db(response_dado_invalido):
    assert not Tarefa.objects.exists()

def test_pagina_com_dados_invalidos(response_dado_invalido):
    assert response_dado_invalido.status_code == 400 #verifica se o status code dá página é o de erro