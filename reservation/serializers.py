from rest_framework import serializers
from .models import *


class ReservationShopSerializer(serializers.RelatedField):
    class Meta:
        model = Shop
        fields = ("id", "name", "logo", "shop_type", "kakaourl")



class ReservationSerializer(serializers.ModelSerializer):
     shop_date = ["shop.id", "shop.name"]
     shop = serializers.ReadOnlyField(source=shop_date)
     user = serializers.ReadOnlyField(source="user.id")



     class Meta:
        model = Reservation
        fields = ("id","state", "reserved_date", "user", "shop")



