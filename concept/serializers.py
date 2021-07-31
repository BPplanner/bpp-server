from rest_framework import serializers
from .models import *

class StudioConceptSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('is_like')

    class Meta:
        model = StudioConcept
        #fields = '__all__' #TODO 테스트끝나면 아래에 id랑 profile로만 보이게수정필요
        #exclude = ('created_at', 'updated_at')
        fields = ('id','profile','shop','like')
    
    def is_like(self,obj):
        if LikeStudioConcept.objects.filter(studio_concept=obj.id,user=self.context['user'].id):
            return "true"
        else:
            return "false"

class OneStudioConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioConcept
        #fields = '__all__'
        #exclude = ('created_at', 'updated_at')
        fields = ('id','profile','shop')

class BeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        #fields = '__all__'
        #exclude = ('created_at', 'updated_at')
        fields = ('id','profile')

class OneBeautyShopConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeautyShopConcept
        #fields = '__all__'
        #exclude = ('created_at', 'updated_at')
        fields = ('id','profile','shop')