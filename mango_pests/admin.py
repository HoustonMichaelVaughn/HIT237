from django.contrib import admin
from .models import FarmBlock, Pest, PestCheck, PlantType

admin.site.register(FarmBlock)
admin.site.register(Pest)
admin.site.register(PestCheck)
admin.site.register(PlantType)