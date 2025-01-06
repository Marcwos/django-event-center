# Generated by Django 4.2.17 on 2025-01-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('servicios', models.TextField(blank=True, null=True, verbose_name='Servicios adicionales')),
            ],
        ),
    ]
