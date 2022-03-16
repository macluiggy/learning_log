"""Define url patterns for users."""
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')), # aqui se matchea las rutas de django como /login, /logout, etc.
    path('register/', views.register, name='register'),
]