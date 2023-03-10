from django.db import models

# Create your models here.

class Empresa(models.Model):
    descripcion= models.CharField(max_length=100)
    telefono   = models.CharField(max_length=100,default='')
    email      =models.EmailField()
    def __str__(self):
        return self.descripcion

