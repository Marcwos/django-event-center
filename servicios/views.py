from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm  # Necesitas crear este formulario

def is_owner(user):
    return user.role == 'admin' and user.is_verified

@user_passes_test(is_owner)
def manage_services(request):
    services = Service.objects.filter(owner=request.user)
    return render(request, 'servicios/manage_services.html', {'services': services})

@user_passes_test(is_owner)
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.owner = request.user
            service.save()
            return redirect('manage_services')
    else:
        form = ServiceForm()
    return render(request, 'servicios/add_service.html', {'form': form})

@user_passes_test(is_owner)
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, owner=request.user)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('manage_services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'servicios/edit_service.html', {'form': form})

@user_passes_test(is_owner)
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, owner=request.user)
    if request.method == 'POST':
        service.delete()
        return redirect('manage_services')
    return render(request, 'servicios/delete_service.html', {'service': service})

def list_services(request):
    services = Service.objects.all()
    return render(request, 'servicios/servicios.html', {'services': services})