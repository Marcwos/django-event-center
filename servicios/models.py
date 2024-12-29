from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', folder='mi-proyecto/services/')  # Cambiado a CloudinaryField
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title
