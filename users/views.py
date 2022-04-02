"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer

# Models
from users.models import User

class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'


    @action(detail=False, methods=['post'])
    def login(self, request):
        """Login o sign in de un usuario"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        # print(data)
        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Registro o Creacion del usuario"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)