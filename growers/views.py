from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm

class Login(LoginView):
    template_name = "growers/login.html"

class RegisterUser(FormView):
    template_name = "growers/register.html"
    success_url = reverse_lazy("login")
    form_class = RegisterUserForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
@login_required
def profile_view(request):
    return render(request, 'growers/profile.html')