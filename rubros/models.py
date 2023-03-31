from django.db import models
from empresa.models import Empresa

class Rubros(models.Model):
    descripcion=models.CharField(max_length=100)
    empresa   = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True,related_name="rubros_empresa",blank=True)
    menu       = models.BooleanField(default=True)
    order     = models.IntegerField(default=0)
    imagen=models.ImageField(upload_to="rubros",null=True, blank=True)
    def __str__(self):
        return self.descripcion

