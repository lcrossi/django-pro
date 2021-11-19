from django.test import Client


def test_home_status_code(client:Client):
    resposta = client.get('/') #fazendo uma requisição para a página home... ela retorna um código de status"
    assert resposta.status_code == 200 #Validando a resposta
