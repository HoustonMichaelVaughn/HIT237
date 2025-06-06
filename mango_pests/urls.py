# mango_pests/urls.py

from django.urls import path, re_path
from mango_pests.surveillance.views import summary_view
from . import views


urlpatterns = [
    re_path(r"^$", views.home, name="home"),

    path("about/", views.AboutView.as_view(), name="about"),
    path("pestlist/", views.PestListView.as_view(), name="pestlist"),

    # detail view for the pest 
    re_path(
        r"^pestlist/(?P<slugurl>[a-zA-Z-]+)/?$",
        views.PestDetailView.as_view(),
        name="pest_detail",
    ),

    path("references/", views.ReferencesView.as_view(), name="references"),
    path("pest/new/", views.create_pest, name="create_pest"),
    path("farmblock/new/", views.add_farm_block, name="add_farm_block"),
    path("pestcheck/new/", views.create_pest_check, name="create_pest_check"),

    path(
        "pestcheck/<int:pk>/edit/",
        views.PestCheckUpdateView.as_view(),
        name="edit_pest_check",
    ),
    path(
        "pestcheck/<int:pk>/delete/",
        views.PestCheckDeleteView.as_view(),
        name="delete_pest_check",
    ),

    path(
        "farmblock/<int:pk>/edit/",
        views.FarmBlockUpdateView.as_view(),
        name="edit_farm_block",
    ),
    path(
        "farmblock/<int:pk>/delete/",
        views.FarmBlockDeleteView.as_view(),
        name="delete_farm_block",
    ),

    
    path("surveillance/summary/", summary_view, name="surveillance-summary"),
]
