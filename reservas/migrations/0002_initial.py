# Generated by Django 4.2.17 on 2025-01-05 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salones', '0001_initial'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='salones.salon', verbose_name='Salón reservado'),
        ),
    ]
