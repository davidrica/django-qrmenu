# Generated by Django 4.1.7 on 2023-03-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_articulos_empresa_articulos_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='receta',
            field=models.TextField(blank=True, default=''),
        ),
    ]