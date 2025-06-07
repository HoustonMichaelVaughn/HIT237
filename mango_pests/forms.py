from django import forms
from mango_pests.models import Pest
from .data import Pestsdiseases
from .models import PATH_CHOICES, FarmBlock, PestCheck, PlantType


class SampleSizeForm(forms.Form):
    prevalence = forms.FloatField(
        label="Assumed prevalence (e.g. 0.01 = 1%)",
        initial=0.01,
        min_value=0.0001,
        max_value=0.5,
        required=True,
    )
    confidence = forms.FloatField(
        label="Desired confidence level (e.g. 0.95 = 95%)",
        initial=0.95,
        min_value=0.5,
        max_value=0.9999,
        required=True,
    )


class PestCheckForm(forms.ModelForm):
    path_pattern = forms.ChoiceField(
        choices=PATH_CHOICES,
        label="Inspection Pattern",
        widget=forms.Select(
            attrs={"class": "form-control", "aria-describedby": "pathHelp"}
        ),
    )
    pest = forms.ChoiceField(label="Pest")

    class Meta:
        model = PestCheck
        fields = [
            "farm_block",
            "date_checked",
            "part_of_plant",
            "infestation_level",
            "path_pattern",
            "num_trees",
            "positives",
            "notes",
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["farm_block"].queryset = FarmBlock.objects.filter(grower=user)
        else:
            self.fields["farm_block"].queryset = FarmBlock.objects.none()
        db_pests = list(Pest.objects.all())
        static_pests = [
            (f"static::{i}", p.cardtitle) for i, p in enumerate(Pestsdiseases)
        ]
        db_choices = [(str(p.pk), p.name) for p in db_pests]
        self.fields["pest"].choices = db_choices + static_pests

    def clean_pest(self):
        value = self.cleaned_data["pest"]
        if value.startswith("static::"):
            return value
        try:
            return Pest.objects.get(pk=value)
        except (Pest.DoesNotExist, ValueError, TypeError):
            raise forms.ValidationError("Invalid pest selection.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        pest_val = self.cleaned_data.get("pest")
        if isinstance(pest_val, str) and pest_val.startswith("static::"):
            instance._static_pest = pest_val
            if commit:
                raise ValueError("Cannot save PestCheck with static pest directly. Handle in view.")
            return instance
        instance.pest = pest_val
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class PestSelectionForm(forms.Form):
    pest = forms.ModelChoiceField(
        queryset=Pest.objects.all(), label="Select a pest to evaluate", required=True
    )


class FarmBlockForm(forms.ModelForm):
    class Meta:
        model = FarmBlock
        fields = ["name", "location_description"]


class PestForm(forms.ModelForm):
    class Meta:
        model = Pest
        fields = ["name", "scientific_name", "description", "plant_type", "image"]
