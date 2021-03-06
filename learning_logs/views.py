from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import EntryForm, TopicForm

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html') # render toma dos argumentos, el request y el nombre del template, esta vela por la carpeta base: templates, entoces el path real es: __dirname/learning_logs/templates/learning_logs/index.html

@login_required # esto es un decorador, un decorador es una funcion que se ejecuta antes de que se ejecute la funcion que tiene abajo, esta sirve para alterar la funcion en cuestion, en este caso se usa @login_required para que solo los usuarios registrados puedan acceder a la funcion topics, si no estan logueados se redirecciona a la pagina de login
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Make sure the topic belongs to the current user.
    # if topics.owner != request.user:
    #     raise Http404
    # print(topics.all())
    context = {'topics': topics} # context es un diccionario que se va a pasar a la plantilla para que pueda ser usado en la plantilla, las keys son los nombres de las variables que se van a usar en la plantilla, en este caso topics, y los values son los valores son los datos que necesitamos pasar a la plantilla.
    return render(request, 'learning_logs/topics.html', context) # render toma dos argumentos, el request y el nombre del template, esta vela por la carpeta base: templates, entoces el path real es: __dirname/learning_logs/templates/learning_logs/topics.html

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    print(topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid(): # checkea que todos los datos esten disponibles y sean validos
            new_topic =  form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # commit=False es para que no guarde el objeto en la base de datos, solo lo crea en memoria, para que luego se guarde en la base de datos.
            new_entry.topic = topic # lo anterior es para poder asignarle el topic al nuevo objeto entry
            new_entry.save() # ahora si, guarda el objeto en la base de datos
            return redirect('learning_logs:topic', topic_id=topic_id) # redirecciona a la pagina de topic con el id del topic que se acaba de crear

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """"Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry) # instance es para que pre-llene el form con los datos del objeto entry que se esta editando
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST) # instance es para que pre-llene el form con los datos del objeto entry que se esta editando y data es para que pre-llene el form con los datos que se estan enviando en el request
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404