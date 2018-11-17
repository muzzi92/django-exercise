from django.test import TestCase
from .models import Restaurant
import requests_mock

# Create your tests here.


class TestRestaurantApi(TestCase):

    def test_stores_api_object_as_attribute(self):
        with requests_mock.mock() as requests:
            requests.get("https://api.myjson.com/bins/19vode/", json={"foo": "bar"})
            nandos = Restaurant("https://api.myjson.com/bins/19vode/")
            self.assertEqual(nandos.information, {"foo": "bar"})

    def test_menu_returns_items(self):
        with requests_mock.mock() as m:
            api_content = {
                "categories": [{
                    "name": "Appeteasers",
                    "menu-items": [{"name": "3 Chicken Wings"}],
                }]
            }
            m.get("https://api.myjson.com/bins/19vode/", json=api_content)
            nandos = Restaurant("https://api.myjson.com/bins/19vode/")
            self.assertEqual(nandos.menu(), ["3 Chicken Wings"])
