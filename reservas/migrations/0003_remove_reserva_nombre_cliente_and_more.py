# Generated by Django 4.2.17 on 2025-01-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='nombre_cliente',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='servicios',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='salon',
            field=models.CharField(max_length=100),
        ),
    ]
