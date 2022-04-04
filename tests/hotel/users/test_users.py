# Django
from django.test import TestCase

# Python
from PIL import Image
import tempfile
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from src.users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            email='testing_login@hotel.bo',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

    def test_signup_user(self):
        """Verificamos si podemos crear un user"""

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        client = APIClient()
        response = client.post(
            '/users/signup/', 
            {
                'email': 'testing@hotel.bo',
                'password': 'rc{4@qHjR>!b`yAV',
                'password_confirmation': 'rc{4@qHjR>!b`yAV',
                'first_name': 'Testing',
                'last_name': 'Testing',
                'phone': '59170654074',
                'city': 'La Paz',
                'country': 'Bolivia',
                'photo': tmp_file,
                'extract': 'I am a testing',
                'invoice_nit': '4900112014',
                'invoice_name': 'invoice name',
                'username': 'testing1'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {"username":"testing1","first_name":"Testing","last_name":"Testing","email":"testing@hotel.bo"})

    