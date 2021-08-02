from rest_framework import serializers
from .models import *

#StudioConceptSerializer에서 shop 일부 정보만 표시용
class StudioConceptShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')

#studio_concept 전체 목록(컨셉북) 조회
class StudioConceptSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = StudioConcept
        fields = ('id','profile','shop','like')
    
    def is_like(self,obj):
        if LikeStudioConcept.objects.filter(studio_concept=obj.id,user=self.context['user'].id):
            return True
        else:
            return False

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['shop'] = StudioConceptShopSerializer(instance.shop).data #id랑 이름만
        return response

#ShopDetailConcept에서 StudioConcept 일부 정보만 표시용
class OneStudioConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioConcept
        fields = ('id','profile')

#ShopDetailConcept에서 BeautyShopConcept 일부 정보만 표시용
class OneBeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        fields = ('id','profile')