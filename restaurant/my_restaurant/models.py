from django.db import models

# Create your models here.

class Orders(models.Model):
    table_number = models.IntegerField()
    item = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.item