from rest_framework import serializers
from .models import *

class StudioConceptShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')

class StudioConceptSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = StudioConcept
        fields = ('id','profile','shop','like')
    
    def is_like(self,obj):
        if LikeStudioConcept.objects.filter(studio_concept=obj.id,user=self.context['user'].id):
            return "true"
        else:
            return "false"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['shop'] = StudioConceptShopSerializer(instance.shop).data #id랑 이름만
        return response

class OneStudioConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioConcept
        fields = ('id','profile','shop')

class BeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        fields = ('id','profile')

class OneBeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        fields = ('id','profile','shop')