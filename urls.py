from django.urls import path
from . import views

# Define app namespace
app_name = 'farm'

# URL patterns for the app
urlpatterns = [
    path('summary/', views.summary, name='summary'),  # Summary page
    path('recent_checks/', views.recent_checks, name='recent_checks'),  # Recent checks page
    path('add_check/', views.add_check, name='add_check'),  # Add new check form
    path('download_csv/', views.download_csv, name='download_csv'),  # CSV download
