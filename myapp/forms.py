from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.forms.fields import CharField
from django.forms.widgets import Textarea

from .models import Receita

class ReceitaForm(forms.ModelForm):
    ingredientes = SimpleArrayField(
        CharField(),
        widget=Textarea(attrs={'placeholder': '3 xícaras de farinha;\n2 ovos;\n3 xícaras de leite'}),
        error_messages={'item_invalid': 'Por favor remova o último ; '},
        help_text="Separe os ingredientes usando ponto e vírgula ;", delimiter=";"
      )


    class Meta:
        model = Receita
        fields = ["titulo", "categoria", "dificuldade", "rendimento", "imagem", "ingredientes", "modo_de_preparo", 'dica']
