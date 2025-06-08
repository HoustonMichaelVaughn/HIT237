from django import forms
from mango_pests.models import Pest, INFESTATION_LEVEL_CHOICES
from .data import Pestsdiseases
from .models import PATH_CHOICES, FarmBlock, PestCheck, PlantType


class SampleSizeForm(forms.Form):
    prevalence = forms.FloatField(label="Prevalence", min_value=0.0001, max_value=0.9999)
    confidence = forms.FloatField(label="Confidence", min_value=0.0001, max_value=0.9999)
    total_trees_available = forms.IntegerField(min_value=1, label="Number of Trees You Can Check")


class PestCheckForm(forms.ModelForm):
    # Real pests from DB
    real_pest = forms.ModelChoiceField(
        queryset=Pest.objects.all(),
        required=False,
        label="Pest (Custom)",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    # Optional static pest selection
    static_pest = forms.ChoiceField(
        required=False,
        label="Pest (Base)",
        choices=[],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    path_pattern = forms.ChoiceField(
        choices=PATH_CHOICES,
        label="Inspection Pattern",
        widget=forms.Select(attrs={"class": "form-control", "aria-describedby": "pathHelp"})
    )

    infestation_level = forms.ChoiceField(
        choices=[("", "Select infestation level")] + INFESTATION_LEVEL_CHOICES,
        required=False,
        label="Infestation Level",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = PestCheck
        fields = [
            "farm_block",
            "real_pest",
            "static_pest",
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

        self.fields["static_pest"].choices = [("", "Choose a base pest")] + [
            (f"static::{i}", p.cardtitle) for i, p in enumerate(Pestsdiseases)
        ]

    def clean(self):
        cleaned_data = super().clean()
        real_pest = cleaned_data.get("real_pest")
        static_pest = cleaned_data.get("static_pest")

        if not real_pest and not static_pest:
            raise forms.ValidationError("You must select either a custom pest or a base pest.")

        if real_pest and static_pest:
            raise forms.ValidationError("Choose only one pest source: custom OR base.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        real_pest = self.cleaned_data.get("real_pest")
        static_pest = self.cleaned_data.get("static_pest")

        if static_pest:
            instance._static_pest = static_pest
            if commit:
                raise ValueError("Cannot save PestCheck with static pest directly. Handle this in the view.")
            return instance

        if real_pest:
            instance.pest = real_pest

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
        fields = ["name", "location_description", "stocking_rate", "area_hectares"]


class PestForm(forms.ModelForm):
    class Meta:
        model = Pest
        fields = ["name", "scientific_name", "description", "plant_type", "image"]
