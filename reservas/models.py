# reservas/models.py
from django.db import models
from salones.models import Salon  # Importar el modelo Salon desde la app salones

class Reserva(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)  # Relación con Salon
    cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.salon.nombre} para el {self.fecha}"
