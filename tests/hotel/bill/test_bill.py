#django
from rest_framework import status
from .test_bill_factory import TestBillFactory
from src.booking.models import Booking
from datetime import date, timedelta
from faker import Faker

class CreateBookingTest(TestBillFactory):

    def test_room_can_be_unavailable_after_reservation(self):
        booking = self.booking_factory()
        reservation_data = {
            "debit": 100,
            "credit": 0,
            "booking":  booking.id,
            "bill_type": "Efectivo",
            "date": "2022-04-10 09:00"
        }

        response = self.client.post(self.url, reservation_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
