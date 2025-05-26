from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm

class Login(DjangoLoginView):
    template_name = "growers/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

class RegisterUser(FormView):
    template_name = "growers/register.html"
    success_url = reverse_lazy("profile")
    form_class = RegisterUserForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

@login_required
def profile_view(request):
    return render(request, "growers/profile.html")
