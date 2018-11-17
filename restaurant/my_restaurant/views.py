from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests

from .models import Orders, Restaurant

# Create your views here.
def index(request):
    restaurant = Restaurant("https://api.myjson.com/bins/19vode/")
    context = {
        "menu": restaurant.menu(),
        "restaurant_name": restaurant.information["restaurant-info"]["name"],
    }
    return render(request, "my_restaurant/index.html", context)

def order(request):
    table_number = int(request.POST["table_number"])
    for order in request.POST.getlist("choice[]"):
        choice = Orders(item=order, table_number=table_number)
        choice.save()
    return HttpResponseRedirect(reverse("screen"))

def screen(request):
    orders = Orders.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, "my_restaurant/order_screen.html", context)
