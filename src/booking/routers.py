from rest_framework.routers import DefaultRouter
from src.booking.api import BookingViewSet

router = DefaultRouter()
router.register('', BookingViewSet, basename='booking')

urlpatterns = router.urls