from django.urls import path
from .views import summary_view, download_csv
#   This was Neolisa's. I tried to implement it but it's intresting. The download_csv function is non-existent
#   If you are a marker reading this, I forgot to finish this lol.

app_name = "surveillance"


urlpatterns = [
    path("summary/", summary_view, name="summary"),
    path("download_csv/", download_csv, name="download_csv"),
]