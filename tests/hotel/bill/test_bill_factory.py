#django
from rest_framework.test import APITestCase

from tests.factory.bills_factory import BillFactory
from tests.factory.booking_factory import BookingFactory

class TestBillFactory(APITestCase):

    def setUp(self):
        self.url = '/bills/'
        self.bills_factory = BillFactory
        self.booking_factory = BookingFactory
        return super().setUp()

    def tearDown(self):
        return super().tearDown()





