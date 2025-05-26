from django.contrib.auth.models import User 
from django.db import models

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
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE, related_name='pests')
    image = models.ImageField(upload_to='pests/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class PestCheck(models.Model):
    farm_block = models.ForeignKey(FarmBlock, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    date_checked = models.DateField()
    part_of_plant = models.CharField(max_length=100)
    num_trees_checked = models.PositiveIntegerField()
    num_positive = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    @property
    def confidence_score(self):
        """Calculates and returns a simple confidence percentage"""
        if self.num_trees_checked == 0:
            return None  # Avoid division by zero
        return round((self.num_positive / self.num_trees_checked) * 100, 1)

    def __str__(self):
        return f"{self.pest.name} at {self.farm_block.name} on {self.date_checked}"