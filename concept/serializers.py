from rest_framework import serializers
from .models import *

class StudioConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioConcept
        #fields = '__all__'
        #exclude = ('created_at', 'updated_at')
        fields = ('id','profile')

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