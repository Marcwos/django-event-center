from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('usuarios.urls')),
    path('', include('contact.urls')),
    path('', include('servicios.urls')),
    path('', include('reservas.urls')),
]
