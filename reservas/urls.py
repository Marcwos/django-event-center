from django.urls import path
from . import views

urlpatterns = [
    path('fechas/', views.seleccionar_fechas, name='seleccionar_fechas'),
    path('salon/', views.seleccionar_salon, name='seleccionar_salon'),
    path('services/', views.seleccionar_servicios, name='seleccionar_servicios'),
    path('resumen/', views.resumen_reserva, name='resumen_reserva'),
]
