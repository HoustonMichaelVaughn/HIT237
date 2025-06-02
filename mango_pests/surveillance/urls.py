from django.urls import path
from .views import summary_view, download_csv

app_name = "surveillance"


urlpatterns = [
    path("summary/", summary_view, name="summary"),
    path("download_csv/", download_csv, name="download_csv"),
]