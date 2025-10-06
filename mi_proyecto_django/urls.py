# mi_proyecto_django/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 💡 Incluye todas las rutas de la app 'frontend'
    # Esta debe ser la última ruta para que React maneje todas las URLs
    path('', include('frontend.urls')), 
]