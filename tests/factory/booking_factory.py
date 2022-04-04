import random
import factory
from faker import Faker
from datetime import date, timedelta
from src.rooms.models import Room
from src.booking.models import Booking

from .room_factory import RoomFactory

fake = Faker()

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    state = 'Pendiente'
    room = factory.SubFactory(RoomFactory)
    bookingDate = date.today() + timedelta(days=1)
    arrivalDate = date.today() + timedelta(days=3)
    day_of_stay = 3
    



