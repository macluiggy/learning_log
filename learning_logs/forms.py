from django import forms

from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # el modelo del que se basa el formulario
        fields = ['text'] # del modelo, solo incluye el campo text
        labels = {'text': ''} # no generes a label para el campo text

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry # el modelo del que se basa el formulario
        fields = ['text'] # del modelo, solo incluye el campo text
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # customize the input field for the text field.