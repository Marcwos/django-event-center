from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    verification_code = models.CharField(max_length=6, blank=True, null=True)  # Código de verificación
    is_verified = models.BooleanField(default=False)  # Estado de verificación
    cedula = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Cedula única

    def __str__(self):
        return self.username
