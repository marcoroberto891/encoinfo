from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from inscricoes.models import User , Inscricao , Pessoa , Evento


# serialers define API  representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'login', 'senha',)

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    #User = UserSerializer(many = False)
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'cpf','id_user','is_admin' ,)

'''class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=True)
    class Meta:
        model = Agenda
        fields = ('id', 'visivel', 'usuario', 'usercreator', 'tipo', 'institucional',)

class AgendaSerializerbyUser(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Agenda
        fields = ('id', 'visivel', 'usuario', 'usercreator', 'tipo', 'institucional',)

class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compromisso
        fields = ('id', 'nome', 'datahorainicial', 'datahorafim', 'agenda',)

class AgendaCompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgendaCompromisso
        fields = ('id', 'agenda', 'compromisso', 'usuarios', 'compartilhar', 'useradmin' ,'checkin',)

class AgendaCompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgendaCompromisso
        fields = ('id', 'agenda', 'compromisso', 'usuarios', 'compartilhar', 'useradmin' ,'checkin',)

class AgendaUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgendaUsuario
        fields = ('id', 'agenda', 'usuarios', 'compartilhar', 'useradmin' ,)'''