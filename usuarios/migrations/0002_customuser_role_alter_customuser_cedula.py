# Generated by Django 5.1.3 on 2024-12-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('editor', 'Editor'), ('viewer', 'Viewer')], default='viewer', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cedula',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
