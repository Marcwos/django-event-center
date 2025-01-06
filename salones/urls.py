from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_salones, name='salones'),
    path('crear-salon/', views.crear_salon, name='crear_salon'),
    path('manage_salones/', views.manage_salones, name='manage_salones'),
    path('editar_salon/<int:salon_id>/', views.edit_salon, name='edit_salon'),
    path('eliminar_salon/<int:salon_id>/', views.delete_salon, name='delete_salon'),
]

