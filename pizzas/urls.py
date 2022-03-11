from sys import path_hooks
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('home_pizzas', views.index, name='home_pizzas'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]