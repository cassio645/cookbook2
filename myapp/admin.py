from django.contrib import admin
from .models import Categoria, Receita

class ReceitaAdmin(admin.ModelAdmin):
    model = Receita
    list_display = ("titulo", "autor", "categoria")

admin.site.register(Categoria)
admin.site.register(Receita, ReceitaAdmin)