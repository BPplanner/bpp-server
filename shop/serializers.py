from django.db.models import fields
from rest_framework import serializers
from .models import *
from concept.serializers import *

class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','profile')

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','address','minprice','profile')
        #exclude = ('created_at', 'updated_at', 'shop_type', 'like_users')

class OneShopSerializer(serializers.ModelSerializer):
    #studio_concepts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    concepts = StudioConceptSerializer(source='studio_concepts', many=True)
    affiliates = AffiliateSerializer(read_only=True, many=True)
    class Meta:
        model = Shop
        fields = ('id','name','address_detail','minprice','logo','profile','map','kakaourl','concepts','affiliates')