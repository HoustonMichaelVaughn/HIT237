from django.urls import path, re_path
from . import views

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
    path("pest/new/", views.create_pest, name="create_pest"),
]
