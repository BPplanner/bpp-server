from django.db import models
from multiselectfield import MultiSelectField

class StudioConcept(models.Model):
    HEAD_COUNT_CHOICE = (
        ('one',)
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="concepts")
    shop_name = models.CharField()
    profile = models.ImageField()
    head_count = models.
