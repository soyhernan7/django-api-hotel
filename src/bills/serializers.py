from rest_framework import serializers

from src.bills.models import Bill
from src.booking.models import Booking
from src.booking.serializers import BookingSerializer
from datetime import  date

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'debit', 'credit', 'booking', 'bill_type','date']
        
    def create(self, validated_data):
        """ Metodo invokado al crear la reserva """
        bill = Bill(**validated_data)
        bill.save()
        return bill
    
    def validate(self, data):
        """ Metodo invokado antes de crear la reserva y validarla """        
        return data
        
    def to_representation(self, instance):
        """ Metodo invokado para listar reserva """
        return {
            'id': instance.id,
            'debit': instance.debit,
            'credit': instance.credit,
            'booking': instance.booking.__str__(),
            'bill_type': instance.id,
            'date': instance.id,
        }

class BillPaymentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'