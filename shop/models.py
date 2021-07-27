from django.db import models
from login.models import *
#from reservation.models import *

class Shop(TimeStampMixin):
    STUDIO = 0 #0 대신 SHOP.STUDIO로 쓰기위해
    BEAUTYSHOP = 1
    SHOP_TYPE_CHOICES = (
        (STUDIO, 'studio'),
        (BEAUTYSHOP, 'beautyshop'),
    )

    ADDRESS_CHOICES = (
        ('강남구','강남구'),
        ('강동구','강동구'),
        ('광진구','광진구'),
        ('마포구','마포구'),
        ('서초구','서초구')
    )

    name = models.CharField(max_length=20)
    address = models.CharField(max_length = 20,choices=ADDRESS_CHOICES)
    address_detail = models.TextField(max_length=50)
    minprice = models.IntegerField()
    price_desc = models.ImageField(blank=True, null=True)
    profile = models.ImageField(blank=True, null=True) #컨셉중에서 대표사진
    kakaourl = models.URLField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    shop_type = models.IntegerField(choices=SHOP_TYPE_CHOICES)  # 0 : studio, 1 : beautyshop
    like_users = models.ManyToManyField(User,related_name="like_shops", blank=True, null=True)
    like_count = models.IntegerField(default=0)
    #pick_users = models.ManyToManyField(User, through='Reservation', related_name="pick_shops") #reservation에 중개모델

    def __str__(self):
        return self.name