from django import forms
from .models import PestCheck, FarmBlock

class PestCheckForm(forms.ModelForm):
    # I’m adding a dropdown so growers can pick their inspection pattern
    INSPECTION_PATTERN_CHOICES = [
        ('W', 'W-pattern sweep'),
        ('Z', 'Z-pattern sweep'),
        ('R', 'Random spots'),
    ]
    path_pattern = forms.ChoiceField(
        choices=INSPECTION_PATTERN_CHOICES,
        label="Inspection Pattern",
        help_text="Choose how you walked through the block.",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = PestCheck
        fields = [
            'farm_block',
            'pest',
            'date_checked',
            'part_of_plant',
            'infestation_level',
            'path_pattern',   # ← added this one 
            'notes',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['farm_block'].queryset = FarmBlock.objects.filter(grower=user)
        else:
            self.fields['farm_block'].queryset = FarmBlock.objects.none()

