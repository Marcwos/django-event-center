from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Salon
from .forms import SalonForm

# Verificar si el usuario es admin o editor
def is_owner(user):
    return user.is_staff or user.groups.filter(name='Editor').exists()

def lista_salones(request):
    # Recuperar salones desde la base de datos
    salones = Salon.objects.all()

    # Verificar si el usuario puede agregar salones
    can_add_salon = is_owner(request.user)

    return render(request, 'salones/salones.html', {'salones': salones, 'can_add_salon': can_add_salon})

@user_passes_test(is_owner)
def crear_salon(request):
    if request.method == "POST":
        form = SalonForm(request.POST, request.FILES)
        if form.is_valid():
            salon = form.save(commit=False)
            salon.owner = request.user
            salon.save()
            return redirect('manage_salones')  # Redirigir a la vista de gestión
    else:
        form = SalonForm()
    return render(request, 'salones/crear_salon.html', {'form': form})

@login_required
def manage_salones(request):
    salones = Salon.objects.filter(owner=request.user)
    return render(request, 'salones/manage_salones.html', {'salones': salones})


@user_passes_test(is_owner)
def edit_salon(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id, owner=request.user)
    if request.method == 'POST':
        form = SalonForm(request.POST, request.FILES, instance=salon)
        if form.is_valid():
            form.save()
            return redirect('manage_salones')
    else:
        form = SalonForm(instance=salon)
    return render(request, 'salones/edit_salon.html', {'form': form})


@user_passes_test(is_owner)
def delete_salon(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id, owner=request.user)
    if request.method == 'POST':
        salon.delete()
        return redirect('manage_salones')
    return render(request, 'salones/delete_salon.html', {'salon': salon})
