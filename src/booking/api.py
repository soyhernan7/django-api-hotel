from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status

from src.booking.serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset =  BookingSerializer.Meta.model.objects.all()