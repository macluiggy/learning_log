from django.shortcuts import render
from .models import Pizza
# Create your views here.

def index(req):
  """The home page for Learning Log"""
  return render(req, 'pizzas/index.html')

def pizzas(req):
  """Show all pizzas"""
  pizzas = Pizza.objects.all()
  context = {'pizzas': pizzas}
  return render(req, 'pizzas/pizzas.html', context)

def pizza(req, pizza_id):
  """Show a single pizza and all its toppings"""
  pizza = Pizza.objects.get(id=pizza_id)
  toppings = pizza.topping_set.all()
  context = {'pizza': pizza, 'toppings': toppings}
  
  return render(req, 'pizzas/pizza.html', context)