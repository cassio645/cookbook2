from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .models import Receita, Categoria
from .forms import ReceitaForm


class IndexView(ListView):
    model = Receita
    context_object_name = 'receitas'
    paginate_by = 9

    # iniciando a categoria com None
    categoria = None

    def get_queryset(self):
        # query set recebendo todas as receitas
        queryset = Receita.objects.all()

        # pegando a categoria selecionada pelo filtro(se houver)
        categoria_slug = self.kwargs.get("slug")
        if categoria_slug:
            # caso haja ele vai filtrar o queryset com a categoria desejada
            self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
            # reescrevendo o queryset
            queryset = queryset.filter(categoria=self.categoria)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # categoria selecionada
        context["categoria"] = self.categoria
        # todas as categorias
        context["categorias"] = Categoria.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class MinhasReceitas(ListView):
    model = Receita
    context_object_name = 'receitas'
    template_name = "myapp/receita_minhas.html"
    paginate_by = 9

    def get_queryset(self):
        # filtrando receitas apenas daquele usuário
        return Receita.objects.filter(autor=self.request.user)


class DetalheView(DetailView):
    # nome que vai ser chamado no template
    context_object_name = 'receita'
    queryset = Receita.objects.all()


@method_decorator(login_required, name="dispatch")
class CriarView(CreateView):
    model = Receita
    form_class = ReceitaForm
    success_url = reverse_lazy("receitas:home")

    def form_valid(self, form):
        # pega o usuário logado atualmente e coloca como autor da receita
        form.instance.autor = self.request.user
        return super(CriarView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditarView(UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = "myapp/receita_edit.html"
    success_url = reverse_lazy('receitas:home')

@login_required()
def delete_receita(request, pk):
    receita = Receita.objects.get(pk=pk)
    user = User.objects.get(username=request.user)

    user_delete = str(user).lower().strip()
    autor_receita = str(receita.autor).lower().strip()
    if autor_receita == user_delete:
        receita.delete()
    return redirect('receitas:minhas')


def sobre(request):
    return render(request, 'myapp/about.html')