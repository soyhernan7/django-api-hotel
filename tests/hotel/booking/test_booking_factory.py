#django
from rest_framework.test import APITestCase

from tests.factory.booking_factory import BookingFactory
from tests.factory.room_factory import RoomFactory

class TestBookingFactory(APITestCase):

    def setUp(self):
        self.url = '/booking/'
        self.booking_factory = BookingFactory
        self.room_factory = RoomFactory

        return super().setUp()

    def tearDown(self):
        return super().tearDown()





