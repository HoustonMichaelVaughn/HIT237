from django import forms
from .models import Pest

class PestForm(forms.ModelForm):
    class Meta:
        model = Pest
        fields = ['name', 'scientific_name', 'description', 'plant_type', 'image']