from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

class SignupView(View):

    def get(self, request):
        # Cria o formulário de registro vazio
        context = {"form": RegisterForm()}
        return render(request, "registration/register.html", context)
    
    def post(self, request):
        # Cria um form com os dados do POST
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            # Mensagem após o registro bem-sucedido
            msg = "Você já pode fazer login"

            # Exibindo a mensagem
            messages.info(request, msg)

            return redirect('login')
        
        # Se o formulário não for válido, re-renderizar o template de registro com erros
        context = {"form": form}
        return render(request, "registration/register.html", context)
