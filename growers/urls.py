from django.contrib import admin
from django.urls import path
from .views import Login, RegisterUser, profile_view

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", profile_view, name="profile")
]