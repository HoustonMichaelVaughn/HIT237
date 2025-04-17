from django.urls import path, re_path
from . import views, include

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
    path('', include('mango_pests.urls')),
]