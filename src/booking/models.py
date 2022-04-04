import random
import datetime

from django.db import models
from src.users.models import User
from src.rooms.models import Room
# from src.base.models import BaseModel


class Booking(models.Model):
    """Work Booking model."""
    STATE_CHOICES = (
        ('Pendiente','Pendiente'),
        ('Pagado', 'Pagado'),
        ('Eliminado','Eliminado'),
    )
    state = models.CharField(max_length=15, choices=STATE_CHOICES,null=False,default='Pendiente')
    bookingDate = models.DateField('Fecha de reserva', auto_now=False, auto_now_add=False, blank=False, null=False)
    arrivalDate =models.DateField('Fecha de llegada', auto_now=False, auto_now_add=False, blank=False, null=False)
    day_of_stay = models.IntegerField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room ID',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='User ID',null=True)
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
    def departureDate(self):        
        return (self.arrivalDate + datetime.timedelta(days=self.day_of_stay))
    
    def __str__(self):        
        return f'{self.id} | {self.state} |  {self.bookingDate}'  
