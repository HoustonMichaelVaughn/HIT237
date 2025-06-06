from math import exp

from django.contrib.auth.models import User
from django.db import models

PATH_CHOICES = [
    ("ZigZag", "Zig-Zag between rows"),
    ("Cross", "Cross-row random sample"),
    ("Edge", "Edge perimeter only"),
]


class FarmBlock(models.Model):
    grower = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location_description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.grower.username})"


class PlantType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pest(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    plant_type = models.ForeignKey(
        PlantType, on_delete=models.CASCADE, related_name="pests"
    )
    image = models.ImageField(upload_to="pests/", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class PestCheck(models.Model):
    farm_block = models.ForeignKey(FarmBlock, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    date_checked = models.DateField()
    part_of_plant = models.CharField(max_length=100)
    infestation_level = models.TextField(blank=True)
    num_trees = models.PositiveIntegerField(help_text="Total number of trees checked.")
    positives = models.PositiveIntegerField(
        help_text="Number of trees with visible pest signs."
    )
    notes = models.TextField(blank=True)

    # New Field: Path Pattern
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
        if self.num_trees == 0 or self.positives is None:
            return None
        if self.positives > 0:
            return 0.0
        prevalence = 0.01
        confidence = 1 - exp(-prevalence * self.num_trees)
        return round(confidence * 100, 2)
