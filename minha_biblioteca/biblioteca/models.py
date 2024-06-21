from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()

    # Relacionando o livro ao usuário
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
