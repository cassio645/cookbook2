from django.contrib import admin
from .models import Categoria, Receita

# Area admin cria 
class ReceitaAdmin(admin.ModelAdmin):
    model = Receita

    # Em Receitas aparece em forma tabelar, o titulo, autor e a categoria
    list_display = ("titulo", "autor", "categoria")

admin.site.register(Categoria)
admin.site.register(Receita, ReceitaAdmin)