from django.db.models import fields
from rest_framework import serializers
from .models import *
from concept.serializers import *


class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'profile_1')


class ShopSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'minprice', 'profile_1', 'like')
        # exclude = ('created_at', 'updated_at', 'shop_type', 'like_users')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return "true"
        else:
            return "false"


class OneStudioSerializer(serializers.ModelSerializer):
    # studio_concepts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    concepts = StudioConceptSerializer(source='studio_concepts', many=True)
    affiliates = AffiliateSerializer(read_only=True, many=True)
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = Shop
        fields = (
        'id', 'name', 'address_detail', 'minprice', 'logo', 'profile_1', 'profile_2', 'profile_3', 'like', 'map',
        'kakaourl', 'concepts', 'affiliates')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return "true"
        else:
            return "false"


class OneBeautyShopSerializer(serializers.ModelSerializer):
    # studio_concepts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    concepts = BeautyShopConceptSerializer(source='beautyshop_concepts', many=True)
    affiliates = AffiliateSerializer(read_only=True, many=True)
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = Shop
        fields = (
        'id', 'name', 'address_detail', 'minprice', 'logo', 'profile_1', 'profile_2', 'profile_3', 'map', 'kakaourl',
        'concepts', 'affiliates', 'like')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return "true"
        else:
            return "false"