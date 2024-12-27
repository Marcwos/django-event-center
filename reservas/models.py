from django.db import models
from cloudinary.models import CloudinaryField


class Reserva(models.Model):
    fecha = models.DateField()
    salon = models.CharField(max_length=100)

    def __str__(self):
        return f"Reserva para {self.salon} el {self.fecha}"
    
class Photo(models.Model):
    image= CloudinaryField('image')