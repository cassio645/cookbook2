# Generated by Django 3.2.9 on 2023-08-10 18:01

import ckeditor.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35, unique=True)),
                ('slug', models.SlugField(max_length=35, unique=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=35)),
                ('dificuldade', models.CharField(choices=[('fácil', 'Fácil'), ('mediana', 'Mediana'), ('complexa', 'Complexo')], max_length=8)),
                ('rendimento', models.PositiveSmallIntegerField(help_text='Nº de porções')),
                ('imagem', models.URLField(max_length=1000, verbose_name='Imagem')),
                ('ingredientes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('modo_de_preparo', ckeditor.fields.RichTextField()),
                ('dica', models.CharField(blank=True, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receitas', to='myapp.categoria')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
