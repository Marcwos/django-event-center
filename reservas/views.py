
from django.shortcuts import render, redirect
from .models import Reserva
from django.http import HttpResponseBadRequest
from django.db.models import Count
from servicios.models import Service
from django.contrib.auth.decorators import user_passes_test, login_required
from reservas.models import  Reserva
from salones.models import Salon
 
@login_required
def seleccionar_fechas(request):
    reservas = Reserva.objects.values('fecha').annotate(total=Count('salon'))
    context = {'reservas': list(reservas)}
    return render(request, "reservas/seleccionar_fechas.html", context)

@login_required
def seleccionar_salon(request):
    cadena_fechas = request.GET.get('fecha', '')
    if not cadena_fechas:
        return HttpResponseBadRequest("Se requiere el parámetro 'fecha'.")

    fechas_seleccionadas = [fecha for fecha in cadena_fechas.split(',') if fecha]
    request.session['fechas'] = fechas_seleccionadas

    salones_no_disponibles = Reserva.objects.filter(
        fecha__in=fechas_seleccionadas
    ).values_list('salon', flat=True).distinct()

    # Obtener todos los salones disponibles
    salones = Salon.objects.all()

    context = {
        'salones_no_disponibles': salones_no_disponibles,
        'salones': salones
    }

    if request.method == 'POST':
        salon_nombre = request.POST.get('salon')
        if not salon_nombre:
            context['error'] = 'Debes seleccionar un salón.'
            return render(request, 'reservas/seleccionar_salon.html', context)

        # Buscar la instancia del salón por su nombre
        try:
            salon = Salon.objects.get(nombre=salon_nombre)
        except Salon.DoesNotExist:
            context['error'] = f'El salón "{salon_nombre}" no existe.'
            return render(request, 'reservas/seleccionar_salon.html', context)

        request.session['salon'] = salon.id  # Guardar el ID del salón en la sesión

        for fecha_str in fechas_seleccionadas:
            if Reserva.objects.filter(fecha=fecha_str, salon=salon).exists():
                context['error'] = f'El salón {salon.nombre} ya está reservado para la fecha {fecha_str}.'
                return render(request, 'reservas/seleccionar_salon.html', context)

        return redirect('reservas:seleccionar_servicios')

    return render(request, 'reservas/seleccionar_salon.html', context)


@login_required
def seleccionar_servicios(request):
    services = Service.objects.all()
    if request.method == 'POST':
        # Guarda los IDs de los servicios seleccionados
        servicios_ids = request.POST.getlist('servicios')
        request.session['servicios'] = servicios_ids

        fechas = request.session.get('fechas', [])
        salon_id = request.session.get('salon')

        # Buscar la instancia del salón por su ID
        try:
            salon = Salon.objects.get(id=salon_id)
        except Salon.DoesNotExist:
            return HttpResponseBadRequest("El salón seleccionado no existe.")

        for fecha_str in fechas:
            # Crear la reserva con la instancia del salón
            reserva = Reserva(fecha=fecha_str, salon=salon)
            reserva.save()

        return redirect('reservas:resumen_reserva')

    return render(request, 'reservas/seleccionar_servicios.html', {'services': services})


@login_required
def resumen_reserva(request):
    # Obtener las fechas y el salón desde la sesión
    fechas = request.session.get('fechas', [])
    salon = request.session.get('salon')
    servicios_ids = request.session.get('servicios', [])
    
    try:
        # Convertir los IDs de los servicios a enteros
        servicios_ids = list(map(int, servicios_ids))
    except ValueError:
        return HttpResponseBadRequest("Los datos de los servicios son inválidos.")

    # Filtrar los servicios por sus IDs
    servicios = Service.objects.filter(id__in=servicios_ids)

    # Crear un diccionario para mapear servicios a sus imágenes
    servicios_imagenes = {servicio.id: servicio.image.url for servicio in servicios}

    # Eliminar los datos de la sesión
    del request.session['fechas']
    del request.session['salon']
    del request.session['servicios']

    # Renderizar la plantilla con los datos
    return render(request, 'reservas/resumen_reserva.html', {
        'fecha': ', '.join(fechas),
        'salon': salon,
        'servicios': servicios,
        'servicios_imagenes': servicios_imagenes,
    })
