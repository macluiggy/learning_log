from django.shortcuts import render

# Create your views here.

def index(request):
  """The home page for Learning Log"""
  return render(request, 'learning_logs/index.html') # render toma dos argumentos, el request y el nombre del template, esta vela por la carpeta base: templates, entoces el path real es: __dirname/learning_logs/templates/learning_logs/index.html