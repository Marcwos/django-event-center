from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Salon(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del salón")
    image = CloudinaryField('image', folder='mi-proyecto/salones/')
    capacidad_min = models.PositiveIntegerField(
        verbose_name="Capacidad mínima de personas",
        null=True,
        blank=True,
        help_text="Número mínimo de personas recomendado."
    )
    capacidad_max = models.PositiveIntegerField(verbose_name="Capacidad máxima de personas")
    tiene_escenario = models.BooleanField(default=False, verbose_name="¿Tiene escenario?")
    caracteristicas = models.TextField(
        blank=True,
        null=True,
        verbose_name="Características adicionales",
        help_text="Por ejemplo: Libre vista, cocina, iluminación especial."
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='salones',
        verbose_name="Propietario"
    )

    def __str__(self):
        return self.nombre
