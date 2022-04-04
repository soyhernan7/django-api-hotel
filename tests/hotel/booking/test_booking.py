#django
from rest_framework import status
from .test_booking_factory import TestBookingFactory
from src.rooms.models import Room
from datetime import date, timedelta
class CreateBookingTest(TestBookingFactory):

    def test_room_can_be_unavailable_after_reservation(self):
        """ test para registro de una reserva """

        room = self.room_factory()

        reservation_data = {
            'room': room.id,
            'bookingDate': date.today(),
            'arrivalDate': date.today() + timedelta(days=2),
            "day_of_stay": 2,
            "state": "Pendiente"
        }

        response = self.client.post(self.url, reservation_data)
        room = Room.objects.get(pk=room.id)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
