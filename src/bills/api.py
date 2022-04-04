from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status,mixins
from src.bills.models import Bill

from src.bills.serializers import BillSerializer
from src.bills.serializers import BillPaymentAccountSerializer


class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset =  BillSerializer.Meta.model.objects.all()

class BillPaymentAccountSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    
    serializer_class = BillPaymentAccountSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        """Mandamos por GET una el cliente(user_id), el cuarto (room_id) y nos devuelve un estado de cuenta sencillo
            con todos los pagos realizados para esa reserva (booking)
        """
        user = self.request.query_params.get('user_id', None)
        room = self.request.query_params.get('room_id', None)
        try:
            query = 'select b.id from booking_booking bb \
                    inner join users_user uu on uu.id = bb.user_id \
                    inner join bills_bill b on bb.id = b.booking_id'       
                    
            results = Bill.objects.raw(query, [int(user),int(room)])
        except IntegrityError:
            raise Exception("Sorry, exists a problem with de api BillPaymentAccountSet")            
        return results