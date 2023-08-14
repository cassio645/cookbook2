from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render

from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .helpers import ImagekitClient, ImagekitDelete
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


@login_required
def criar_view(request):

    # SE o método for um post carrega o formulário com as informações dele
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        print(form)

        # Se o formulário for válido(preenchido corretamente)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user

            # IMAGEKIT pega a imagem da receita
            file = request.FILES.get("file")
            
            # Faz upload dela no imagekit e retorna a URL da imagem
            imgkit = ImagekitClient(file)
            response =  imgkit.upload_media_file()
            receita.imagem = response['url']
            receita.file_id = response['fileId']


            # For para pegar todos os ingredientes da receita e transformar num array
            ingredientes = request.POST.getlist('ingredientes')
            receita.ingredientes = ingredientes

            receita.save()

            return redirect('receitas:home')
    else:
        # SE o método for um GET envia o formulário vazio para ser preenchido
        form = ReceitaForm()
  
    return render(request, 'myapp/receita_form.html', {'form': form})


@login_required
def editar_view(request, pk):
    receita = Receita.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)

        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user

            # Atualiza os ingredientes com os novos valores/alterações
            combined_ingredients = request.POST.get("combined_ingredients")
            ingredientes = combined_ingredients.split(", ") if combined_ingredients else []
            receita.ingredientes = ingredientes


            # IMAGEKIT pega a imagem da receita
            file = request.FILES.get("file")

            # Se houver uma nova imagem
            if file:
            
                # Apaga a imagem antiga da receita
                update = ImagekitDelete(receita.file_id)
                update.delete_image()
                
                # Coloca a nova imagem na receita
                imgkit = ImagekitClient(file)
                response =  imgkit.upload_media_file()
                receita.imagem = response['url']
                receita.file_id = response['fileId']

            receita.save()
            return redirect('receitas:home')
    else:
        form = ReceitaForm(instance=receita)

    return render(request, 'myapp/receita_edit.html', {"receita": receita, "form": form})


@login_required()
def delete_receita(request, pk):

    # Pega a receita que vai ser deletada e o usuário que esta querendo deleta-la
    receita = Receita.objects.get(pk=pk)
    user = User.objects.get(username=request.user)

    user_delete = str(user).lower().strip()
    autor_receita = str(receita.autor).lower().strip()

    # Se o usuário for o mesmo autor da receita ele permite, caso contrário só retorna pra página minhas_receitas
    if autor_receita == user_delete:

        # Apaga a imagem antiga da receita e apaga a receita toda
        update = ImagekitDelete(receita.file_id)
        update.delete_image()
        receita.delete()
    return redirect('receitas:minhas')


def sobre(request):
    return render(request, 'myapp/about.html')