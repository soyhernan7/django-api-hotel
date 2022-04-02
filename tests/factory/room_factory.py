import random
import factory
from faker import Faker

from src.rooms.models import Room

fake = Faker()

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    type = random.choice(['Simple', 'Doble', 'Matrimonial','Especial']),
    code = fake.sentence()
    description = fake.sentence()
    price_day = fake.pyint(100, 200)
    discount_rate = fake.pyint(10, 20)
    photo = 'photo/imagen' + str(fake.pyint(10, 20))
    available = True






