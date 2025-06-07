from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mango_pests.urls")),
    path("growers/", include("growers.urls")),
    path(
        "surveillance/",
        include("mango_pests.surveillance.urls", namespace="surveillance"),
    ),
]
