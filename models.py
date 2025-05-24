from django.db import models

class SurveillanceRecord(models.Model):
    check_date = models.DateTimeField(auto_now_add=True)  # Automatically set to current date/time on creation
    confidence = models.FloatField()  # Confidence level of the check (0-100)
    sample_count = models.IntegerField()  # Number of samples taken
    pests_found = models.BooleanField(default=False)  # Whether pests were detected

    def __str__(self):
        # String representation for admin interface
        return f"Check on {self.check_date} - {'Pests found' if self.pests_found else 'No pests'}"
