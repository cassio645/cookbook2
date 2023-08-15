from django import forms
from .models import Receita


class ReceitaForm(forms.ModelForm):
    '''
        Formulário das receitas, criado a partir do model Receita.

        model : Recebe o obj Receita.
        fields : Os campos que fazem parte do formulário.
        widgets : Atributos extras que algum field pode ter.
    '''
    class Meta:
        model = Receita
        fields = ["titulo", "categoria", "dificuldade", "rendimento", "ingredientes", "modo_de_preparo", 'dica']
        widgets = {
            'ingredientes': forms.TextInput(attrs={'placeholder': '3 xícaras de farinha'}),
            'dica': forms.TextInput(attrs={'placeholder': 'Cozinhe em Fogo Baixo'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adicionar classes form-control aos campos
        for field_name in ["titulo", "ingredientes", "modo_de_preparo", "dica"]:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'class': 'form-control'})

        for field_name in ["categoria", "dificuldade", "rendimento"]:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'class': 'select form-control'})

