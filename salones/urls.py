from django.urls import path
from . import views

urlpatterns = [
    path('salones/', views.lista_salones, name='salones'),
]
