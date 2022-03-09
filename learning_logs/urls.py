"""Define URL patterns for learning_logs."""
from django.urls import path 
from . import views

app_name = 'learning_logs' # ayuda a distinguir este archivo urls.py de otro en otras apps dentro del proyecto
urlpatterns = [ # lista de paginas individuales que pueden ser accedidas desde la app learning_logs
  # Home page.
  path('', views.index, name='index'), # el primer argumento una string vacia, es la url que se va a usar para acceder a esta pagina, es como router.route('/') en express, djando recive la url de peticion y  trata de enrutar esa ruta a una view, esto lo hace mediante la busqueda de la url que encaje con la de la peticion del cliente, si no encuentra ninguna url que coincida con la peticion del cliente, entonces se envia una respuesta de error 404, django ignora la base url, es decir que la string vacia encaja con la base url. El segundo argumento es la funcion que se va a ejecutar cuando se acceda a la url, esto es como router.route(/).get(views.index) en express. El tercer argumento es simplemente un nombre de referencia, esto es para poder referenciarlo en otras secciones de codigo en lugar de escribit la url.
  # Page that shows all topics.
  path('topics', views.topics, name='topics'),
  path('topics/<int:topic_id>', views.topic, name='topic'),
]