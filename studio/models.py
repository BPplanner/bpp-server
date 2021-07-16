from django.db import models
from multiselectfield import MultiSelectField

class Shop(models.Model):
    name = models.CharField()
    address = models.TextField(max_length=50)
    minprice = models.IntegerField()
    price_desc = models.ImageField()
    profile = models.ImageField()
    kakaourl = models.URLField()
    logo = models.ImageField()
    shop_type = models.IntegerField()



