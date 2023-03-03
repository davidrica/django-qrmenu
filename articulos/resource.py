from import_export import resources
from .models import Articulos  

class ArticulosResource(resources.ModelResource):  
   class Meta:  
     model = Articulos
     fields = ('codigo', 'descripcion', 'precio',)