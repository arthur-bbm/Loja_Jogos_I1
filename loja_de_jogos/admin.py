from django.contrib import admin

from loja_de_jogos.models import Jogo, Desenvolvedor, Plataforma

# Register your models here.

admin.site.register(Jogo)
admin.site.register(Desenvolvedor)
admin.site.register(Plataforma)