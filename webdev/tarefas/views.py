from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from webdev.tarefas.forms import TarefaNovaForm

# Create your views here.

def home(request):
    if request.method == 'POST': #testa o tipo da requisição
        form = TarefaNovaForm(request.POST) #Usa o formulário criado para validar os dados
        if form.is_valid(): #valida os dados do formulário
            form.save() #Salva os dados dentro do banco
            return HttpResponseRedirect(reverse('tarefas:home')) #redireciona para a home
        else: #Se o formulário é inválido
            return render(request, 'tarefas/home.html', {'form': form}, status=400)

    return render(request, 'tarefas/home.html')
