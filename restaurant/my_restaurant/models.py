from django.db import models


class Orders(models.Model):
    table_number = models.IntegerField()
    item = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item
