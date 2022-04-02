from rest_framework import viewsets

from src.rooms.serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset =  RoomSerializer.Meta.model.objects.all()

