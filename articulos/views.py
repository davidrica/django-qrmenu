from http.client import HTTPResponse
import pandas as pd
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, FormView,CreateView,DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
#from django.utils import timezone
#from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset 

#from utils.mixins import IsAdminMixin

#from comentarios.models import Comentarios
from .models import Articulos
from rubros.models import Rubros
from .forms import ArticuloForm
from rubros.models import Rubros

import os


 

class Listado(ListView):
    template_name = "articulos/listado.html"
    model = Articulos
    context_object_name = "Articulos"
    paginate_by = 50

    def get_queryset(self):
        #my_date = datetime.datetime(2012, 2, 12)
        articulos = Articulos.objects.all()
        
        #parametros = {}
        
        #titulo   = self.request.GET.get("buscador")
        #cat      = self.request.GET.get("categoria")
        #fecha    = self.request.GET.get("fecha")
        #if titulo:
        #    parametros["titulo__contains"]= titulo
#            parametros['titulo__contains']=
        #if fecha:
        #    date = parse_date(fecha)
            
        #    parametros["fecha__gte"]= my_date.combine(date, datetime.time(0, 0)) 
        #    parametros["fecha__lte"]= my_date.combine(date, datetime.time(23, 59)) 
            
        #if cat !='0' and cat is not None:
       
        #    parametros["categoria"]= cat

        
        #articulos = articulos.filter(**parametros)
    
   
        
        return articulos.order_by('descripcion',"rubro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context




#class Editar(LoginRequiredMixin, IsAdminMixin, UpdateView):   
class Editar(UpdateView):   
    model         = Articulos 
    template_name = "articulos/editar.html"
    form_class    = ArticuloForm     

    def get_success_url(self):
        return reverse("Articulos:listado")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context


 
def Importar(request):  
    data = None
    
    template_name = 'articulos/importar.html' 
    if request.method == 'POST' :
        


        dataset = Dataset()
        if 'xlsrubos' in request.FILES:
            filerubros = request.FILES['xlsrubos']
            data_rubros = dataset.load(filerubros.read())
            
            for row in data_rubros:
                
                descripcion ,a,b,c,d,h,i= row
                existe= Rubros.objects.filter(descripcion=descripcion)
                if not existe:
                    Rubros.objects.create(descripcion=descripcion)        
                else:
                    existe.update(descripcion=descripcion)


        if 'xlsarticulos' in request.FILES:
            rubro = Rubros.objects.first()
           
            fileartis = request.FILES['xlsarticulos']
            data_import = dataset.load(fileartis.read())

            for row in data_import:
                codigo, descripcion,precio = row
                existe= Articulos.objects.filter(codigo=codigo)
            
                if not existe:
                    Articulos.objects.create(codigo=codigo, descripcion=descripcion,rubro=rubro,precio=precio)        
                else:
                    existe.update(descripcion=descripcion,precio=precio)

        #result = Employee.import_data(data_import,dry_run=True,raise_errors=True)
        #if not result.has_errors():
        #    Employee.import_data(dataset,dry_run=False)        
    
          
    contexto = {}
    return render(request, template_name, contexto)



def ver_menu(request, id_producto):
    arti = Articulos.objects.filter(pk=id_producto)
    if not arti.menu:
        arti.update(menu=not arti.menu)
    return HttpResponseRedirect(reverse("inicio"))
