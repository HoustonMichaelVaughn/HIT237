from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
	path('about/', views.about, name="about"),
    path('pestlist/', views.pestlist, name="pestlist"),
    re_path(r'^pestlist/(?P<slugurl>[a-zA-Z-]+)/?$', views.pest_detail, name='pest_detail'),
]
