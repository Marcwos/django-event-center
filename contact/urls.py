#CODIGO PARA url.py
from django.urls import path
from .views import ContactoView

urlpatterns = [
    path('contacto/', ContactoView.as_view(), name='contacto'),
]
