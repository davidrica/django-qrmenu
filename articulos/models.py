from django.db import models
from rubros.models import Rubros
from empresa.models import Empresa
from sucursales.models import Sucursales

class Articulos(models.Model):
    codigo     = models.IntegerField()
    descripcion= models.CharField(max_length=100)
    receta     = models.TextField(default='',blank=True)

    precio     = models.DecimalField(max_digits=13,decimal_places=2)
    imagen     = models.ImageField(upload_to="rubros",null=True, blank=True)
    menu       = models.BooleanField(default=True)
    # relaciones 
    rubro      = models.ForeignKey(Rubros,on_delete=models.SET_NULL,null=True,related_name="arti_rubros",blank=True)
    sucursal   = models.ManyToManyField(Sucursales)
    empresa   = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True,related_name="articulos_empresa",blank=True)

    #/media/articulos
    #imagen=models.ImageField(upload_to="articulos",null=True, blank=True)
    def __str__(self):
        return self.descripcion


