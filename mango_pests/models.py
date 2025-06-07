# This file defines the database models for the 'mango_pests' app.
# For more information on Django models, visit:
# https://docs.djangoproject.com/en/stable/topics/db/models/

from django.db import models
from django.contrib.auth.models import User

# PATH_CHOICES is used to define sampling methods for pest checks.
# Each tuple contains a machine-readable value and a human-readable label.
PATH_CHOICES = [
    ("ZigZag", "Zig-Zag between rows"),
    ("Cross", "Cross-row random sample"),
    ("Edge", "Edge perimeter only"),
]


class FarmBlock(models.Model):
    """
    Represents a block of farmland associated with a grower.

    Fields:
        - grower: ForeignKey to the User model, representing the owner of the farm block.
        - name: Name of the farm block.
        - location_description: Text description of the farm block's location.

    For more information on ForeignKey, visit:
    https://docs.djangoproject.com/en/stable/ref/models/fields/#foreignkey
    """
    grower = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location_description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.grower.username})"


class PlantType(models.Model):
    """
    Represents the type of plant that can be grown in a farm block.

    Fields:
        - name: The common name of the plant type.

    For more information on model fields, visit:
    https://docs.djangoproject.com/en/stable/ref/models/fields/
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Pest(models.Model):
    """
    Represents a pest that can affect plants in a farm block.

    Fields:
        - name: The common name of the pest.
        - scientific_name: The scientific name of the pest (optional).
        - description: A text description of the pest.
        - plant_type: ForeignKey to the PlantType model, representing the type of plant the pest affects.
        - image: An image of the pest (optional).
        - owner: ForeignKey to the User model, representing the owner of the pest record (optional).

    For more information on model relationships, visit:
    https://docs.djangoproject.com/en/stable/topics/db/models/#relationships
    """
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

    For more information on model methods, visit:
    https://docs.djangoproject.com/en/stable/topics/db/models/#methods
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

        For more information on properties in Django models, visit:
        https://docs.djangoproject.com/en/stable/topics/db/models/#properties
        """
        if self.num_trees == 0 or self.positives is None:
            return None
        if self.positives > 0:
            return 0.0
        prevalence = 0.01
        confidence = 1 - exp(-prevalence * self.num_trees)
        return round(confidence * 100, 2)
