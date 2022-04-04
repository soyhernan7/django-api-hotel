from django.db import models
from src.booking.models import Booking

# django-ckeditor
from ckeditor.fields import RichTextField


class Bill(models.Model):
    """Work Bill model."""
    
    STATE_CHOICES = (
        ('Efectivo','Efectivo'),
        ('Tarjeta Credito', 'Tarjeta Credito'),
        ('Tarjeta Debito','Tarjeta Debito'),
        ('Pasarela de Pago','Pasarela de Pago'),
    )
    debit = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    credit = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField(null=True, max_length=255,choices=STATE_CHOICES)
    date = models.DateTimeField(null=True)

    def __str__(self):        
        return self.uuid
    
    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'