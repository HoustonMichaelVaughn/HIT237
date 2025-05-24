from django import forms
from .models import SurveillanceRecord

# Form for adding new surveillance records
class SurveillanceForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord  # Link to SurveillanceRecord model
        fields = ['confidence', 'sample_count', 'pests_found']  # Fields to include in the form
        labels = {
            'confidence': 'Confidence (%)',  # User-friendly field labels
            'sample_count': 'Sample Count',
            'pests_found': 'Pests Found'
        }
