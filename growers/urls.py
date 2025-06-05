from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Login, RegisterUser, profile_view, export_csv

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/export-csv/", export_csv, name="export_csv"),
]
