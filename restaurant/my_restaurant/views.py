from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Orders, Restaurant

# Create your views here.
def index(request):
    nandos = Restaurant("https://api.myjson.com/bins/19vode/")
    context = {
        'menu': nandos.menu()
    }
    return render(request, 'my_restaurant/index.html', context)

def order(request, order_id):
    order_name = Orders.objects.get(pk=1).item
    return HttpResponse(f"Order {order_id} was for {order_name}")
