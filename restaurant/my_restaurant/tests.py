from django.test import TestCase, Client
from .models import Orders
from . serializers import OrdersSerializer


class TestRestaurantApi(TestCase):

    client = Client()

    def setUp(self):
        Orders.objects.create(
            table_number=22, item="fish heads")
        Orders.objects.create(
            table_number=13, item="beans")

    def test_get_all_orders(self):
        response = self.client.get("http://127.0.0.1:8000/orders/")
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)

        self.assertEqual(response.data, serializer.data)
