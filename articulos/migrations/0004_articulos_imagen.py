# Generated by Django 4.1.7 on 2023-03-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_alter_articulos_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='rubros'),
        ),
    ]