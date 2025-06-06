from django.contrib.auth import views as auth_views
from django.urls import path

from .views import Login, RegisterUser, profile_view
from . import views

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path("ajax/farmblocks/", views.ajax_farm_block_list, name="farm_block_list"),
    path("ajax/pestchecks/", views.ajax_pest_check_list, name="pest_check_list"),
    path("ajax/pests/", views.ajax_pest_list, name="pest_list"),
]
