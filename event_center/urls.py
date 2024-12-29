from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # Página de inicio
    path('usuarios/', include('usuarios.urls')),
    path('contact/', include('contact.urls')),
    path('servicios/', include('servicios.urls')),  # Prefijo para servicios
    path('reservas/', include('reservas.urls')),
    path('salones/', include('salones.urls')),
]
