# Generated by Django 4.1.7 on 2023-03-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0006_alter_sucursales_imagen'),
        ('articulos', '0006_alter_articulos_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='sucursal',
            field=models.ManyToManyField(blank=True, null=True, to='sucursales.sucursales'),
        ),
    ]
