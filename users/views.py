from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

class SignupView(View):
    def get(self, request):
        context = {"form": RegisterForm()}
        return render(request, "registration/register.html", context)
    
    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            msg = "Você já pode fazer login"
            messages.info(request, msg)
            return redirect('login')
        context = {"form":form}
        return render(request, "registration/register.html", context)