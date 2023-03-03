from django.db import models
from rubros.models import Rubros
import datetime
 
class Articulos(models.Model):
    codigo     = models.IntegerField()
    descripcion= models.CharField(max_length=100)
    receta     = models.TextField(default='')
    #rubro      =models.CharField(max_length=50)
    precio     = models.DecimalField(max_digits=13,decimal_places=2)
    rubro      = models.ForeignKey(Rubros,on_delete=models.SET_NULL,null=True,related_name="arti_rubros",blank=True)
    menu       = models.BooleanField(default=True)

    #/media/articulos
    #imagen=models.ImageField(upload_to="articulos",null=True, blank=True)
    def __str__(self):
        return self.descripcion


