from rest_framework import serializers
from .models import *

class PickShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickShop
        fields = '__all__'