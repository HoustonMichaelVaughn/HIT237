"""
URL configuration for mango_pests_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Sources:
# https://www.w3schools.com/django/django_slug_field.php

from django.contrib import admin
from django.urls import path, re_path
from mango_pests import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', v.home, name="home"),
    path('about/', v.AboutView.as_view(), name="about"),
    path('pestlist/', v.PestListView.as_view(), name="pestlist"),
    re_path(r'^pestlist/(?P<slugurl>[a-zA-Z-]+)/?$', v.PestDetailView.as_view(), name='pest_detail')
]
