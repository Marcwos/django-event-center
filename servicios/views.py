from django.shortcuts import render

def servicios(request):
    return render(request, "servicios/servicios.html")
