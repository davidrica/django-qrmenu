from django.db import models
from empresa.models import Empresa
 
class Sucursales(models.Model):
    descripcion = models.CharField(max_length=100)
    url         = models.URLField(max_length=100,default='')
    activa      = models.BooleanField(default=False)
    imagen      = models.ImageField(upload_to="sucursales",null=True, blank=True)
    empresa     = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True,related_name="sucursales_empresa",blank=True)
    def __str__(self):
        return self.descripcion


