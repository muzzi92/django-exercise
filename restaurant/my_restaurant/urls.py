from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('screen/', views.screen, name='screen'),
    path('complete/', views.complete, name='complete'),
    path('delete/', views.delete, name='delete'),
]
