from rest_framework import serializers
from .models import *

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        #fields = '__all__'
        exclude = ('created_at', 'updated_at')