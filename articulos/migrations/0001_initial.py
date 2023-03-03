# Generated by Django 4.1.7 on 2023-03-03 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rubros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('receta', models.TextField(default='')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=13)),
                ('menu', models.BooleanField(default=True)),
                ('rubro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arti_rubros', to='rubros.rubros')),
            ],
        ),
    ]
