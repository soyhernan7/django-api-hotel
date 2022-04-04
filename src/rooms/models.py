import random
from django.db import models

# from src.base.models import BaseModel

class Room(models.Model):
    class RoomTypes(models.TextChoices):
        SIMPLE = 'Simple'
        DOBLE = 'Doble'
        MATRIMONIAL = 'Matrimonial'
        ESPECIAL = 'Especial'

    type = models.CharField('Room Type', max_length=40, choices=RoomTypes.choices, null=False)
    code = models.TextField('Code', blank=False, null=False,default=0)
    description = models.TextField('Description', blank=False, null=False)
    price_day = models.PositiveIntegerField('Price day',default=0)
    photo = models.ImageField(null=True, upload_to='photo')
    discount_rate = models.PositiveIntegerField('Discount Rate',default=0)
    available = models.BooleanField('Available', default=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.type}"

    def get_total_price_day(self):
        return self.price_day - (self.price_day * self.discount_rate)