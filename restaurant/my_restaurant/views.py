from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests

from .models import Orders, Restaurant

# Create your views here.
def index(request):
    nandos = Restaurant("https://api.myjson.com/bins/19vode/")
    context = {
        'menu': nandos.menu()
    }
    return render(request, 'my_restaurant/index.html', context)

def order(request):
    choice = Orders(item=request.POST['choice'], table_number=1)
    choice.save()
    return HttpResponseRedirect(reverse('index'))
