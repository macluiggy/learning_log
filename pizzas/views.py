from django.shortcuts import render

# Create your views here.

def index(req):
  """The home page for Learning Log"""
  return render(req, 'pizzas/index.html')