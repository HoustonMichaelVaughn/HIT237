#comments to ba updated later
from django.urls import path, re_path
from . import views

urlpatterns = [
  re_path(r'^$, views.HomeView.as_view(), name="home"),
  path('about/', views.AboutView.as_view(), name="about"),
  path('pestlist/', views.PestListView.as_view(), name="pestlist"),
  re_path(r'^pestlist/(?P<slugurl>[a-zA-Z-]+)/?$', views.PestDetailView.as_view(), name= 'pest_detail'),
]
