from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nome = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=35, unique=True)

    class Meta:
        ordering = ("nome",)
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("receitas:lista_categoria", kwargs={"slug":self.slug})


class Receita(models.Model):
    DIFICULDADE = (
        ('fácil', "Fácil"),
        ('mediana', "Mediana"),
        ('complexa', "Complexo"),
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=35)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="receitas")
    dificuldade = models.CharField(max_length=8, choices=DIFICULDADE)
    rendimento = models.PositiveSmallIntegerField(help_text="Nº de porções")
    imagem = models.ImageField()
    ingredientes = ArrayField(models.TextField())
    modo_de_preparo = RichTextField()
    dica = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalhe', kwargs={"pk": self.pk})