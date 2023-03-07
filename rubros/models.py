from django.db import models
 
class Rubros(models.Model):
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="rubros",null=True, blank=True)
    def __str__(self):
        return self.descripcion

