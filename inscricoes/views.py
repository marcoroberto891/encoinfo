from django.shortcuts import render
# Create your views here.
from rest_framework import routers , serializers , viewsets
from django.contrib.auth.models import User
from inscricoes.serializers import UserSerializer , PessoaSerializer
from inscricoes.models import User , Pessoa


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

