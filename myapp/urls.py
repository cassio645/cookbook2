from django.urls import path
from . import views


app_name = "receitas"
urlpatterns = [ 
    path("", views.IndexView.as_view(), name="home"),
    path("categoria/<slug:slug>", views.IndexView.as_view(), name="lista_categoria"),
    path("minhas-receitas/", views.MinhasReceitas.as_view(), name="minhas"),
    path("<int:pk>/", views.DetalheView.as_view(), name="detalhe"),
    path("criar/", views.CriarView.as_view(), name="criar"),
    path("editar/<int:pk>/", views.EditarView.as_view(), name="editar"),
    path("deletar/<int:pk>/", views.delete_receita, name="deletar"),
    path("sobre/", views.sobre, name="sobre"),
]