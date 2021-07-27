from django.db.models import fields
from rest_framework import serializers
from .models import *
from concept.serializers import *

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','address','minprice','profile')
        #exclude = ('created_at', 'updated_at', 'shop_type', 'like_users')

class OneShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','address','minprice','profile','affiliates')
        depth = 1