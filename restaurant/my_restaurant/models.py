from django.db import models
import requests
# Create your models here.


class Orders(models.Model):
    table_number = models.IntegerField()
    item = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item


class Restaurant:

    def __init__(self, url):
        self.information = requests.get(url).json()

    def menu(self):
        menu_list = []
        item_categories =  self.information["categories"]
        for category in item_categories:
            items = category["menu-items"]
            for item in items:
                menu_list.append(f"{item['name']} - ₹{item['sub-items'][0]['price']}")
        return menu_list
