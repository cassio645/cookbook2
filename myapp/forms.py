from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.forms.fields import CharField
from django.forms.widgets import Textarea

from .models import Receita


class ReceitaForm(forms.ModelForm):

    class Meta:
        model = Receita
        fields = ["titulo", "categoria", "dificuldade", "rendimento", "ingredientes", "modo_de_preparo", 'dica']
        widgets = {
            'ingredientes': forms.TextInput(attrs={'placeholder': '3 xícaras de farinha'}),
            'dica': forms.TextInput(attrs={'placeholder': 'Cozinhe em Fogo Baixo'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adicionar classes aos campos
        for field_name in ["titulo", "ingredientes", "modo_de_preparo", "dica"]:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'class': 'form-control'})

        for field_name in ["categoria", "dificuldade", "rendimento"]:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'class': 'select form-control'})

