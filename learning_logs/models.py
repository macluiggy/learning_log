from cgitb import text
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