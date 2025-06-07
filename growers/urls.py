from django.urls import path
from django.contrib.auth import views as auth_views

from .views import Login, RegisterUser, profile_view, export_csv
from . import views

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/export-csv/", export_csv, name="export_csv"),
    
    # AJAX endpoints for HTMX
    path("ajax/farmblocks/", views.ajax_farm_block_list, name="farm_block_list"),
    path("ajax/pestchecks/", views.ajax_pest_check_list, name="pest_check_list"),
    path("ajax/pests/", views.ajax_pest_list, name="pest_list"),
]
