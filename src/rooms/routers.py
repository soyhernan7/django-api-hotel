from rest_framework.routers import DefaultRouter
from src.rooms.api import RoomViewSet

router = DefaultRouter()
router.register('', RoomViewSet, basename='rooms')

urlpatterns = router.urls