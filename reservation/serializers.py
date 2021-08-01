from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "state", "reserved_date", "shop")
        depth = 1