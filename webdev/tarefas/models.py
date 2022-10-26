from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    feita =  BooleanField(default=False)

    class Meta:
        verbose_name_plural= 'Tarefas'

        def __str__(self):
            return self.nome