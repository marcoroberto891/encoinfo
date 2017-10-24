from django.contrib import admin
from inscricoes.models import User , Pessoa , Evento , Inscricao
# Register your models here.
admin.site.register(User)
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(Inscricao)