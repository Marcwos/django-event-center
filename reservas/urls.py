from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('fechas/', views.seleccionar_fechas, name='seleccionar_fechas'),
    path('salon/', views.seleccionar_salon, name='seleccionar_salon'),
    path('servicios/', views.seleccionar_servicios, name='seleccionar_servicios'),
    path('resumen_reserva/', views.resumen_reserva, name='resumen_reserva'),
]
