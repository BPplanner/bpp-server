from django.db.models import fields
from rest_framework import serializers
from .models import *
from concept.serializers import *


class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'profile')


class ShopSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'minprice', 'profile', 'like')
        # exclude = ('created_at', 'updated_at', 'shop_type', 'like_users')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return True
        else:
            return False


class OneStudioSerializer(serializers.ModelSerializer):
    # studio_concepts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    concepts = StudioConceptSerializer(source='studio_concepts', many=True)
    affiliates = AffiliateSerializer(read_only=True, many=True)
    like = serializers.SerializerMethodField('is_like')
    profiles = serializers.SerializerMethodField('profile_array')

    class Meta:
        model = Shop
        fields = (
        'id', 'name', 'address_detail', 'minprice', 'logo', 'profiles', 'like', 'map',
        'kakaourl', 'concepts', 'affiliates')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return True
        else:
            return False

    def profile_array(self,obj):
        return [self.context['request'].build_absolute_uri(obj.profile.url), self.context['request'].build_absolute_uri(obj.profile_2.url),
        self.context['request'].build_absolute_uri(obj.profile_3.url)]


class OneBeautyShopSerializer(serializers.ModelSerializer):
    # studio_concepts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    concepts = BeautyShopConceptSerializer(source='beautyshop_concepts', many=True)
    affiliates = AffiliateSerializer(read_only=True, many=True)
    like = serializers.SerializerMethodField('is_like')
    profiles = serializers.SerializerMethodField('profile_array')

    class Meta:
        model = Shop
        fields = (
        'id', 'name', 'address_detail', 'minprice', 'logo', 'profiles', 'like','map',
        'kakaourl','concepts', 'affiliates')

    def is_like(self, obj):
        if LikeShop.objects.filter(shop=obj.id, user=self.context['user'].id):
            return True
        else:
            return False
    
    def profile_array(self,obj):
        return [self.context['request'].build_absolute_uri(obj.profile.url), self.context['request'].build_absolute_uri(obj.profile_2.url),
        self.context['request'].build_absolute_uri(obj.profile_3.url)]