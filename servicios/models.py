from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title

    
class Photo(models.Model):
    # Título descriptivo para la imagen
    title = models.CharField(max_length=100)
    # Campo para almacenar la imagen en Cloudinary
    image = CloudinaryField('image', blank=False)
    # Fecha de creación de la imagen
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
