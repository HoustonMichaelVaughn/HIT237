from django import forms
from .models import PestCheck, FarmBlock, PATH_CHOICES

class PestCheckForm(forms.ModelForm):
    # >>> these share PATH_CHOICES so it stays in sync with the entire model
    path_pattern = forms.ChoiceField(
    choices=PATH_CHOICES,
    label="Inspection Pattern",
    widget=forms.Select(attrs={
        'class': 'form-control',
        'aria-describedby': 'pathHelp'
    })
)


    class Meta:
        model = PestCheck
        fields = [
            'farm_block',
            'pest',
            'date_checked',
            'part_of_plant',
            'infestation_level',
            'path_pattern',
            'num_trees',
            'positives',
            'notes',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['farm_block'].queryset = FarmBlock.objects.filter(grower=user)
        else:
            self.fields['farm_block'].queryset = FarmBlock.objects.none()

