from rest_framework import serializers

from src.booking.models import Booking
from src.rooms.serializers import RoomSerializer
from src.users.serializers import UserSignUpSerializer
from datetime import  date

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'state', 'bookingDate', 'arrivalDate', 'day_of_stay','room','user']
        
    def create(self, validated_data):
        """ Metodo invokado al crear la reserva """
        booking = Booking(**validated_data)
        booking.save()
        return booking
    
    def validate(self, data):
        """ Metodo invokado antes de crear la reserva y validarla """        
        if data['arrivalDate'] < date.today():
            raise serializers.ValidationError(
                {'arrivalDate':"""Debe ser mayor a la fecha de Hoy"""}
            )
        return data
        
    def to_representation(self, instance):
        """ Metodo invokado para listar reserva """
        return {
            'id': instance.id,
            'user': instance.user.__str__(),
            'room': instance.room.__str__(),
            'state': instance.state,
            'bookingDate' : instance.bookingDate,
            'arrivalDate' : instance.arrivalDate,
            'day_of_stay' : instance.day_of_stay,
            'departureDate' : instance.departureDate() ,            
        }
