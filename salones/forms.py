from django import forms
from .models import Salon

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        exclude = ['owner']  # Excluye el campo 'owner'
        labels = {
            'nombre': 'Nombre del salón',
            'image': 'Imagen del salón',
            'capacidad_min': 'Capacidad mínima',
            'capacidad_max': 'Capacidad máxima',
            'tiene_escenario': '¿Tiene escenario?',
            'caracteristicas': 'Características adicionales',
        }
        widgets = {
            'caracteristicas': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ejemplo: Libre vista, cocina...'}),
        }
