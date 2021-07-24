from django.db import models
from login.models import *

class Shop(TimeStampMixin):
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    minprice = models.IntegerField()
    price_desc = models.ImageField()
    profile = models.ImageField()
    kakaourl = models.URLField()
    logo = models.ImageField()
    shop_type = models.IntegerField()  # 0 : studio, 1 : beautyshop
    like_users = models.ManyToManyField(User ,related_name="like_shops")
    #pick_users = models.ManyToManyField(User, through='PickShop', related_name="pick_shops") #reservation에 중개모델