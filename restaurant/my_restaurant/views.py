from rest_framework import viewsets

from .models import Orders
from .serializers import OrdersSerializer

# Create your views here.


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
