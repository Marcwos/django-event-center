from django.shortcuts import render, redirect
from .models import Reserva
from django.http import HttpResponseBadRequest
from django.db.models import Count

def seleccionar_fechas(request):
    reservas = Reserva.objects.values('fecha').annotate(total=Count('salon'))
    context = {'reservas': list(reservas)}
    return render(request, "reservas/seleccionar_fechas.html", context)

def seleccionar_salon(request):
    fecha_string = request.GET.get('fecha', '')
    if fecha_string:
        fechas_seleccionadas = fecha_string.split(',')
        request.session['fechas'] = fechas_seleccionadas
        print("Fechas seleccionadas:", fechas_seleccionadas)

        # Obtener salones no disponibles para las fechas seleccionadas
        salones_no_disponibles = Reserva.objects.filter(
            fecha__in=[fecha for fecha in fechas_seleccionadas if fecha]
        ).values_list('salon', flat=True).distinct()

        print("Salones no disponibles:", list(salones_no_disponibles))  # Depuración

        context = {'salones_no_disponibles': salones_no_disponibles}
    else:
        return HttpResponseBadRequest("Se requiere el parámetro 'fecha'.")

    if request.method == 'POST':
        salon = request.POST.get('salon')
        request.session['salon'] = salon

        for fecha_str in fechas_seleccionadas:
            if fecha_str:
                if Reserva.objects.filter(fecha=fecha_str, salon=salon).exists():
                    print(f"El salón {salon} ya está reservado para la fecha {fecha_str}.")  # Depuración
                    context['error'] = f'El salón {salon} ya está reservado para la fecha {fecha_str}.'
                    return render(request, 'reservas/seleccionar_salon.html', context)

        return redirect('reservas:seleccionar_servicios')

    return render(request, 'reservas/seleccionar_salon.html', context)

def seleccionar_servicios(request):
    if request.method == 'POST':
        servicios = request.POST.getlist('servicios')
        request.session['servicios'] = servicios
        return redirect('reservas:resumen_reserva')
    return render(request, 'reservas/seleccionar_servicios.html')

def resumen_reserva(request):
    fechas = request.session.get('fechas', [])
    salon = request.session.get('salon')
    servicios = request.session.get('servicios')
    return render(request, 'reservas/resumen_reserva.html', {
        'fecha': ', '.join(fechas),
        'salon': salon,
        'servicios': servicios,
    })
