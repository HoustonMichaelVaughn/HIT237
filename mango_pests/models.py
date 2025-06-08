# This file defines the database models for the 'mango_pests' app.
# For more information on Django models, visit:
# https://docs.djangoproject.com/en/stable/topics/db/models/

from django.db import models
from django.contrib.auth.models import User
from math import exp

# PATH_CHOICES is used to define sampling methods for pest checks.
# Each tuple contains a machine-readable value and a human-readable label.
PATH_CHOICES = [
    ("ZigZag", "Zig-Zag between rows"),
    ("Cross", "Cross-row random sample"),
    ("Edge", "Edge perimeter only"),
]


class FarmBlock(models.Model):
    #Represents a block of farmland associated with a grower.

    grower = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location_description = models.TextField()
    stocking_rate = models.PositiveIntegerField(help_text="Number of trees per hectare.", default=100)
    area_hectares = models.DecimalField(max_digits=6, decimal_places=2, help_text="Area of the block in hectares.")

    def __str__(self):
        return f"{self.name} ({self.grower.username})"

    @property
    def estimated_tree_count(self):
        return round(self.area_hectares * self.stocking_rate)


class PlantType(models.Model):
    #Represents the type of plant that can be grown in a farm block.

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pest(models.Model):

    # Represents a pest that can affect plants in a farm block.
    #- name: The common name of the pest.
    #- scientific_name: The scientific name of the pest (optional).
    #- description: A text description of the pest.
    #- plant_type: ForeignKey to the PlantType model, representing the type of plant the pest affects.
    #- image: An image of the pest (optional).
    #- owner: ForeignKey to the User model, representing the owner of the pest record (optional).

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE, related_name="pests")
    image = models.ImageField(upload_to="pests/", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class PestCheck(models.Model):
    """
    Represents a check for pests in a farm block.

    Fields:
        - farm_block: ForeignKey to the FarmBlock model, representing the block where the check was performed.
        - pest: ForeignKey to the Pest model, representing the pest being checked for.
        - date_checked: The date when the pest check was performed.
        - part_of_plant: The part of the plant where the check was performed.
        - infestation_level: A text field describing the level of infestation (optional).
        - num_trees: The total number of trees checked for pests.
        - positives: The number of trees with visible signs of pests.
        - notes: Additional notes about the pest check (optional).
        - path_pattern: The pattern used to walk through the block during the check.
    """
    farm_block = models.ForeignKey(FarmBlock, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    date_checked = models.DateField()
    part_of_plant = models.CharField(max_length=100)
    infestation_level = models.TextField(blank=True)
    num_trees = models.PositiveIntegerField(help_text="Total number of trees checked.")
    positives = models.PositiveIntegerField(help_text="Number of trees with visible pest signs.")
    notes = models.TextField(blank=True)
    path_pattern = models.CharField(
        max_length=20,
        choices=PATH_CHOICES,
        default="ZigZag",
        help_text="Pick your walk pattern through the block.",
    )

    def __str__(self):
        return f"{self.pest.name} at {self.farm_block.name} on {self.date_checked}"

    @property
    def confidence_score(self):
        """
        Calculates the confidence score of the pest check.

        The confidence score is based on the prevalence of the pest and the number of trees checked.
        A higher score indicates a higher confidence in the presence of the pest.
        """
        if self.num_trees == 0 or self.positives is None:
            return None
        if self.positives > 0:
            return 0.0
        prevalence = 0.01
        confidence = 1 - exp(-prevalence * self.num_trees)
        return round(confidence * 100, 2)

    @property
    def sampling_coverage_percent(self):
        try:
            total = self.farm_block.estimated_tree_count
            if not total or total == 0:
                return None
            return round((self.num_trees / total) * 100, 2)
        except (AttributeError, ZeroDivisionError, TypeError):
            return None

    @property
    def sampling_comment(self):
        percent = self.sampling_coverage_percent
        if percent is None:
            return "Coverage unknown"
        if percent >= 20:
            return "Sufficient coverage"
        return "Insufficient coverage"
