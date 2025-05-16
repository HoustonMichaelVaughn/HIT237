from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .views import (
    PestCheckListView,
    PestCheckCreateView,
    PestCheckUpdateView,
    PestCheckDeleteView,
)

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("pestlist/", views.PestListView.as_view(), name="pestlist"),
    re_path(
        r"^pestlist/(?P<slugurl>[a-zA-Z-]+)/?$",
        views.PestDetailView.as_view(),
        name="pest_detail",
    ),
    path("references/", views.ReferencesView.as_view(), name="references"),
    # CRUD routes for PestCheck records
    path("records/", PestCheckListView.as_view(), name="pestcheck_list"),
    path("records/create/", PestCheckCreateView.as_view(), name="pestcheck_create"),
    path("records/<int:pk>/edit/", PestCheckUpdateView.as_view(), name="pestcheck_edit"),
    path("records/<int:pk>/delete/", PestCheckDeleteView.as_view(), name="pestcheck_delete"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path(
        'register/',
        CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/login/'
        ),
        name='register'
    ),
]

