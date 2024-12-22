from django.shortcuts import render

def servicios(request):
    return render(request, "servicios/servicios.html")

def admin_request_service_basic (request):
    return render (request, "servicios/servicios.html")
