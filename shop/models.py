from django.db import models
from login.models import *

class Shop(TimeStampMixin):
    STUDIO = 0 #0 대신 SHOP.STUDIO로 쓰기위해
    BEAUTYSHOP = 1
    SHOP_TYPE_CHOICES = (
        (STUDIO, 'studio'),
        (BEAUTYSHOP, 'beautyshop'),
    )


    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    minprice = models.IntegerField()
    price_desc = models.ImageField(blank=True)
    profile = models.ImageField(blank=True)
    kakaourl = models.URLField(blank=True)
    logo = models.ImageField(blank=True)
    shop_type = models.IntegerField(choices=SHOP_TYPE_CHOICES)  # 0 : studio, 1 : beautyshop
    like_users = models.ManyToManyField(User ,related_name="like_shops")
    pick_users = models.ManyToManyField(User, through='PickShop', related_name="pick_shops") #reservation에 중개모델