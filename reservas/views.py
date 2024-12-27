from django.shortcuts import render, redirect
from .models import Reserva
from django.http import HttpResponseBadRequest
from django.db.models import Count
from servicios.models import Service

def seleccionar_fechas(request):
    reservas = Reserva.objects.values('fecha').annotate(total=Count('salon'))
    context = {'reservas': list(reservas)}
    return render(request, "reservas/seleccionar_fechas.html", context)

def seleccionar_salon(request):
    cadena_fechas = request.GET.get('fecha', '')
    if not cadena_fechas:
        return HttpResponseBadRequest("Se requiere el parámetro 'fecha'.")

    fechas_seleccionadas = [fecha for fecha in cadena_fechas.split(',') if fecha]
    request.session['fechas'] = fechas_seleccionadas

    salones_no_disponibles = Reserva.objects.filter(
        fecha__in=fechas_seleccionadas
    ).values_list('salon', flat=True).distinct()

    context = {'salones_no_disponibles': salones_no_disponibles}

    if request.method == 'POST':
        salon = request.POST.get('salon')
        if not salon:
            context['error'] = 'Debes seleccionar un salón.'
            return render(request, 'reservas/seleccionar_salon.html', context)

        request.session['salon'] = salon

        for fecha_str in fechas_seleccionadas:
            if Reserva.objects.filter(fecha=fecha_str, salon=salon).exists():
                context['error'] = f'El salón {salon} ya está reservado para la fecha {fecha_str}.'
                return render(request, 'reservas/seleccionar_salon.html', context)

        return redirect('reservas:seleccionar_servicios')

    return render(request, 'reservas/seleccionar_salon.html', context)

def seleccionar_servicios(request):
    services = Service.objects.all()
    if request.method == 'POST':
        servicios = request.POST.getlist('servicios')
        request.session['servicios'] = servicios

        fechas = request.session.get('fechas', [])
        salon = request.session.get('salon')

        for fecha_str in fechas:
            reserva = Reserva(fecha=fecha_str, salon=salon)
            reserva.save()

        return redirect('reservas:resumen_reserva')

    return render(request, 'reservas/seleccionar_servicios.html', {'services': services})

def resumen_reserva(request):
    fechas = request.session.get('fechas', [])
    salon = request.session.get('salon')
    servicios = request.session.get('servicios')

    del request.session['fechas']
    del request.session['salon']
    del request.session['servicios']

    return render(request, 'reservas/resumen_reserva.html', {
        'fecha': ', '.join(fechas),
        'salon': salon,
        'servicios': servicios,
    })
