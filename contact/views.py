#CODIGO PARA views.py
from django.shortcuts import render

def contacto(request):
    return render(request, 'contacto.html')
