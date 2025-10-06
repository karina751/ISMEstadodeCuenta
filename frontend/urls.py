# frontend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mapea la ruta raíz de la aplicación ('') a la función 'index' en views.py
    path('', views.index),
]