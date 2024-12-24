from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def seleccionar_fechas(request):
    return render(request,"reservas/seleccionar_fechas.html")

def seleccionar_salon(request):
    if request.method == 'POST':
        salon = request.POST.get('salon')
        request.session['salon'] = salon
        return redirect('seleccionar_servicios')
    return render(request, 'reservas/seleccionar_salon.html')


def seleccionar_servicios(request):
    if request.method == 'POST':
        servicios = request.POST.getlist('servicios')
        request.session['servicios'] = servicios
        return redirect('resumen_reserva')
    return render(request, 'reservas/seleccionar_servicios.html')


def resumen_reserva(request):
    fecha = request.session.get('fecha')
    salon = request.session.get('salon')
    servicios = request.session.get('servicios')
    return render(request, 'reservas/resumen_reserva.html', {
        'fecha': fecha,
        'salon': salon,
        'servicios': servicios,
    })
