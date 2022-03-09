from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html') # render toma dos argumentos, el request y el nombre del template, esta vela por la carpeta base: templates, entoces el path real es: __dirname/learning_logs/templates/learning_logs/index.html

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    # print(topics.all())
    context = {'topics': topics} # context es un diccionario que se va a pasar a la plantilla para que pueda ser usado en la plantilla, las keys son los nombres de las variables que se van a usar en la plantilla, en este caso topics, y los values son los valores son los datos que necesitamos pasar a la plantilla.
    return render(request, 'learning_logs/topics.html', context) # render toma dos argumentos, el request y el nombre del template, esta vela por la carpeta base: templates, entoces el path real es: __dirname/learning_logs/templates/learning_logs/topics.html

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    print(topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)