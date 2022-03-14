from django.contrib import admin

# Register your models here.
from .models import Entry, Topic # el punto . es para importar el modelo desde el mismo directorio que el archivo admin.py, esto es como ./ para importar un JavaScript

admin.site.register(Topic) # registra el modelo Topic a traves del administrador de Django
admin.site.register(Entry) # registra el modelo Entry a traves del administrador de Django
