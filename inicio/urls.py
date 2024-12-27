from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('salones/', views.lista_salones, name='salones'),
]
