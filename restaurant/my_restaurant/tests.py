from django.test import TransactionTestCase, Client
from django.core.exceptions import ObjectDoesNotExist
from .models import Orders
from .serializers import OrdersSerializer


class TestRestaurantApi(TransactionTestCase):

    client = Client()
    reset_sequences = True

    def setUp(self):
        Orders.objects.create(table_number=22, item="fish heads")
        Orders.objects.create(table_number=13, item="beans")

    def test_get_all_orders(self):
        response = self.client.get("http://127.0.0.1:8000/orders/")
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_delete_order(self):
        response = self.client.delete("http://127.0.0.1:8000/orders/1/")
        self.assertRaises(ObjectDoesNotExist, Orders.objects.get, id=1)

    def test_get_order_by_id(self):
        response = self.client.get("http://127.0.0.1:8000/orders/1/")
        order = Orders.objects.get(pk=1)
        serializer = OrdersSerializer(order)

        self.assertEqual(response.data, serializer.data)

    def test_create_order(self):
        response = self.client.post(
            "http://127.0.0.1:8000/orders/", {"table_number": 6, "item": "bread"}
        )
        order = Orders.objects.get(table_number=6)

        self.assertEqual(order.item, "bread")
