# frontend/views.py

from django.shortcuts import render

def index(request):
    # Esta función busca 'index.html' dentro de la carpeta 'templates/frontend'
    return render(request, 'frontend/index.html')