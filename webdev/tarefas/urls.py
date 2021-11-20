from django.contrib import admin
from django.urls import path
from django.urls import include
from webdev.tarefas import views

app_name='tarefas'

urlpatterns = [
    path('', views.home, name='home'),
]