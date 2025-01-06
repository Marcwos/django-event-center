# Generated by Django 4.2.17 on 2025-01-05 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0002_initial'),
        ('reservas', '0003_remove_reserva_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cliente',
            field=models.CharField(default='Desconocido', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salones.salon'),
        ),
    ]
