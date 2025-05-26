from django import forms
from .models import Pest
from .models import FarmBlock
from .models import PestCheck
from django import forms
from mango_pests.models import Pest

class SampleSizeForm(forms.Form):
    prevalence = forms.FloatField(
        label="Assumed prevalence (e.g. 0.01 = 1%)",
        initial=0.01,
        min_value=0.0001,
        max_value=0.5,
        required=True
    )
    confidence = forms.FloatField(
        label="Desired confidence level (e.g. 0.95 = 95%)",
        initial=0.95,
        min_value=0.5,
        max_value=0.9999,
        required=True
    )
    
class PestCheckForm(forms.ModelForm):
    class Meta:
        model = PestCheck
        fields = ['farm_block', 'pest', 'date_checked', 'part_of_plant',
                  'num_trees_checked', 'num_positive', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['farm_block'].queryset = FarmBlock.objects.filter(grower=user)

class PestSelectionForm(forms.Form):
    pest = forms.ModelChoiceField(
        queryset=Pest.objects.all(),
        label="Select a pest to evaluate",
        required=True
    )

class FarmBlockForm(forms.ModelForm):
    class Meta:
        model = FarmBlock
        fields = ['name', 'location_description']

class PestForm(forms.ModelForm):
    class Meta:
        model = Pest
        fields = ['name', 'scientific_name', 'description', 'plant_type', 'image']
