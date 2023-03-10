
from django.views.generic import ListView, UpdateView, FormView,CreateView,DeleteView
from django.urls import reverse


from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SucursalesForm

from utils.mixins import IsAdminMixin


from .models import Sucursales

from django.utils.six import BytesIO

 

class Listado(LoginRequiredMixin, IsAdminMixin,ListView):
    template_name = "sucursales/listado.html"
    model = Sucursales
    context_object_name = "Sucursales"
    paginate_by = 50

    def get_queryset(self):
        mi_empresa = self.request.user.empresa
        suc = Sucursales.objects.all()
        parametros = {}
        parametros["empresa"]= mi_empresa
        titulo   = self.request.GET.get("buscador")
        #cat      = self.request.GET.get("rubro")
        #fecha    = self.request.GET.get("fecha")
        if titulo:
            parametros["descripcion__contains"]= titulo
        #    parametros["descripcion__icontains"]= titulo
#            parametros['titulo__contains']=
        #if fecha:
        #    date = parse_date(fecha)
            
        #    parametros["fecha__gte"]= my_date.combine(date, datetime.time(0, 0)) 
        #    parametros["fecha__lte"]= my_date.combine(date, datetime.time(23, 59)) 
            
        #if cat !='0' and cat is not None:
       
        #    parametros["rubro"]= cat

        
        suc = suc.filter(**parametros)
    
   
        
        return suc.order_by('descripcion')


class Editar(LoginRequiredMixin, IsAdminMixin, UpdateView):   
#class Editar(UpdateView):   
    model         = Sucursales 
    template_name = "sucursales/editar.html"
    form_class    = SucursalesForm  

    def get_success_url(self):
        return reverse("Sucursales:listado")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context
