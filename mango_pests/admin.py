from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import FarmBlock, Pest, PestCheck, PlantType

for model in (PlantType, Pest, FarmBlock, PestCheck):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        # if some other admin.py already registered it, this will just skip it
        pass
