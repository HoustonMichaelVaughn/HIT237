from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm
from django.contrib.auth import login


class Login(LoginView):
    template_name = "growers/login.html"

class RegisterUser(FormView):
    template_name = "growers/register.html"
    sucess_url = "/"
    form_class = RegisterUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.re)
        return super().form_valid(form)