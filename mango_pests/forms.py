from django import forms
from .models import PestCheck, FarmBlock

class PestCheckForm(forms.ModelForm):
    class Meta:
        model = PestCheck
        fields = ['farm_block', 'pest', 'date_checked', 'part_of_plant', 'infestation_level', 'notes']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # Limit the FarmBlock queryset to those owned by the logged in user
            self.fields['farm_block'].queryset = FarmBlock.objects.filter(grower=user)
        else:
            # If no user is passed, default to empty queryset
            self.fields['farm_block'].queryset = FarmBlock.objects.none()
