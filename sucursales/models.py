from django.db import models
from empresa.models import Empresa
 
class Sucursales(models.Model):
    descripcion= models.CharField(max_length=100)
    url= models.URLField(max_length=100,default='')
    empresa   = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True,related_name="sucursales_empresa",blank=True)
    def __str__(self):
        return self.descripcion


