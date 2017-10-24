from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField('login',max_length=100)
    senha = models.CharField('senha',max_length=6)


class Pessoa(models.Model):
    nome = models.CharField('nome',max_length=100)
    cpf = models.CharField('cpf',max_length=11)
    is_admin = models.ForeignKey(User, related_name='Pessoa_is_admin', null=True,blank=False)

class Evento(models.Model):
    nome = models.CharField('nome',max_length=50)
    descricao = models.CharField('cpf',max_length=100)
    dataInicio = models.DateField()
    dataFim = models.DateField()

class Inscricao(models.Model):
    nome = models.CharField('nome',max_length=100)
    cpf = models.CharField('cpf',max_length=11)
    is_admin = models.ForeignKey(User, related_name='Inscricao_is_admin', null=True,blank=False)

