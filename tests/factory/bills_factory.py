import random
import factory
from faker import Faker
from datetime import date, timedelta
from src.booking.models import Booking
from src.bills.models import Bill
from .booking_factory import BookingFactory

fake = Faker()

class BillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bill

    booking = factory.SubFactory(BookingFactory)
    debit = factory.LazyAttribute(lambda x: random.randrange(10, 100))
    credit = factory.LazyAttribute(lambda x: random.randrange(10, 100))
    bill_type = "Efectivo",
    date = date.today()
    



