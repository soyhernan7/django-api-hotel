from rest_framework.routers import DefaultRouter
from src.bills.api import BillViewSet,BillPaymentAccountSet

router = DefaultRouter()
router.register('', BillViewSet, basename='booking')
router.register(r'bill_payment_account', BillPaymentAccountSet, basename='bill')

urlpatterns = router.urls