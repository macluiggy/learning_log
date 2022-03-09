from sys import path_hooks
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('pizzas', views.index, name='index'),
]