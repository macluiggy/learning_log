from cgitb import text
from operator import truediv
from pickle import TRUE
from django.db import models

# Create your models here.
class Topic(models.Model):
  """A topic the user is learning about."""
  text = models.CharField(max_length=200) # CharField is a field that stores a string, and it has a max_length attribute.
  date_added = models.DateTimeField(auto_now_add=True) # record date and time

  def __str__(self):
    """Return a string representation of the model."""
    return f"{self.text}"

class Entry (models.Model):
  """Something specific learned about a topic."""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ForeignKey is a field that stores a reference to another model. The cascade option is used to delete all the entries relalated to the topic when the topic object is deleted. see https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey
  text = models.TextField() # TextField is a field that stores a large string of text.
  date_added= models.DateTimeField(auto_now_add=True) # record date and time

  class Meta:
    verbose_name_plural = 'entries' # verbose_name_plural is a special attribute that Django uses to pluralize the name of the model. For example, if you set the verbose_name to 'entry' Django will use the verbose_name_plural of 'entries'. but withouth this attribute Django will use the verbose_name of 'Entry' as 'Entrys' which is misspelled.
  def __str__(self):
    """Return a string representation of the model."""
    return f"{self.text[:50]}..." if len(self.text) > 50 else self.text # return the first 50 characters of the text field if the text field is longer than 50 characters.