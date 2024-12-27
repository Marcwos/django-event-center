#CODIGO PARA url.py
from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
]
