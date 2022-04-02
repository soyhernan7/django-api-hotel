from rest_framework import serializers

from src.rooms.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type', 'code','description','price_day', 'photo', 'discount_rate', 'available']