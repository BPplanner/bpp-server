from django.db import models
from shop.models import *

class BeautyShopConcept(models.Model):
    profile = models.ImageField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="concepts")
    
