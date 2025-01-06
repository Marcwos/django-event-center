# Generated by Django 4.2.17 on 2025-01-05 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salones', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salones', to=settings.AUTH_USER_MODEL, verbose_name='Propietario'),
        ),
    ]