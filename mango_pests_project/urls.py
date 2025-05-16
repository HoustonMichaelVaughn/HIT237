from django.contrib import admin
from django.urls import path, re_path, include
from mango_pests import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mango_pests.urls')), 
]
