from rest_framework import serializers
from .models import *


class ReservationShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'shop_type', 'name', 'logo',)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "state", "reserved_date", "shop")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['shop'] = ReservationShopSerializer(instance.shop, context={"request": self.context['request']}).data
        return response
