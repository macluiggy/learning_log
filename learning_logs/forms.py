from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # el modelo del que se basa el formulario
        fields = ['text'] # del modelo, solo incluye el campo text
        labels = {'text': ''} # no generes a label para el campo text