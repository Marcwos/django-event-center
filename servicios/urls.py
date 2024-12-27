from django.urls import path
from . import views

urlpatterns = [
    path('manage-services/', views.manage_services, name='manage_services'),
    path('add/', views.add_service, name='add_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>/', views.delete_service, name='delete_service'),
    path('', views.list_services, name='list_services'),  # Nueva ruta para listar servicios
    path('upload/', views.upload_photo, name='subirfoto'),

]
