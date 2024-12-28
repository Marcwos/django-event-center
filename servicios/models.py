from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title



from cloudinary.models import CloudinaryField
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image')  # Este campo manejará la subida a Cloudinary automáticamente
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title