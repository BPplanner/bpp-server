from django.db.models import fields
from rest_framework import serializers
from .models import *

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        exclude = ('created_at', 'updated_at')