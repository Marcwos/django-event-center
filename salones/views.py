from django.shortcuts import render

def lista_salones(request):
    salones = [
        {
            'nombre': 'Salón Plaza',
            'imagen': 'https://via.placeholder.com/300',  # URL de imagen temporal
            'tamano': 'Grande',
            'capacidad': 100,
            'tiene_escenario': True,
            'libre_vista': True,
            'salon_de_cocina': True,
        },
        {
            'nombre': 'Salón Imperial',
            'imagen': 'https://via.placeholder.com/300',
            'tamano': 'Mediano',
            'capacidad': 60,
            'tiene_escenario': False,
            'libre_vista': True,
            'salon_de_cocina': False,
        },
        # Agrega más salones si deseas
    ]
    return render(request, 'salones.html', {'salones': salones})

