#django
from rest_framework import status
from .test_rooms_factory import TestRoomsFactory
from src.rooms.models import Room

class CreateRoomsTest(TestRoomsFactory):
  
    def test_room1_can_record_room(self):
        """ Puede registrar un cuarto """
        response = self.client.post(self.url, self.room_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_room2_can_not_record_with_no_field_type(self):
        """ No Puede registrar un cuarto sin tipo de cuarto """
        response = self.client.post(self.url, { 'price': 50 })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_room3_can_view_a_room(self):
        """ Puede ver un cuarto en particular en la url : /api/rooms/1"""
        room = self.room_factory.create()
        response = self.client.get(f'{self.url}{room.id}/')        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], room.id)

    def test_room4_can_view_all_rooms(self):
        """ Puede listar todos los cuartos """
        for _ in range(5):
            self.room_factory.create()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 5)


