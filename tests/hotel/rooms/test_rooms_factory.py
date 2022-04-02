#django
from rest_framework.test import APITestCase
from tests.factory.room_factory import RoomFactory

# Python
from PIL import Image
import tempfile

class TestRoomsFactory(APITestCase):

    def setUp(self):
        """ Dato de prueba para generar un cuarto, generamos una imagen de prueba para
        los rooms """
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        
        self.url = '/rooms/'
        self.room_factory = RoomFactory
        self.room_data = {
            'type': 'Simple',
            'code': 'A1',
            'description': 'A1',                        
            'price_day': 150,
            'discount_rate':10,
            'photo': tmp_file,
            'available':True
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()



