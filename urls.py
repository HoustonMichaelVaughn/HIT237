from django.urls import path
from . import views

app_name = 'surveillance'

urlpatterns = [
    # Route for recent checks view
    path('recent_checks/', views.recent_checks, name='recent_checks'),
    # Route for summary view
    path('summary/', views.summary, name='summary'),
    # Route for CSV download
    path('download_csv/', views.download_csv, name='download_csv'),
]
