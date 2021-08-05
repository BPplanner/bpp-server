from rest_framework import serializers
from .models import *


# ReservationSerializer에서 shop에 필요한 정보만 표시하기 위해
class ReservationShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'shop_type', 'name', 'logo',)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "state", "reserved_date", "shop")

    def to_representation(self, instance): #shop에서 필요한 정보만 표시
        response = super().to_representation(instance)
        response['shop'] = ReservationShopSerializer(instance.shop, context={"request": self.context['request']}).data
        return response
