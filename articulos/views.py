from http.client import HTTPResponse
import pandas as pd
from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView, UpdateView, FormView,CreateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
#from django.utils import timezone
#from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset 

from utils.mixins import IsAdminMixin

#from comentarios.models import Comentarios
from .models import Articulos
from rubros.models import Rubros
from sucursales.models import Sucursales
from .forms import ArticuloForm
from rubros.models import Rubros
   

from django.utils.six import BytesIO
import qrcode

import os
from django.http import FileResponse
from utils.mixins import is_admin_required
 

class Listado(LoginRequiredMixin, IsAdminMixin,ListView):
    template_name = "articulos/listado.html"
    model = Articulos
    context_object_name = "Articulos"
    paginate_by = 50

    def get_queryset(self):
        
        #my_date = datetime.datetime(2012, 2, 12)
        articulos = Articulos.objects.all()
        
        parametros = {}
        
        titulo   = self.request.GET.get("buscador")
        cat      = self.request.GET.get("rubro")
        #fecha    = self.request.GET.get("fecha")
        if titulo:
            ##parametros["descripcion__contains"]= titulo
            parametros["descripcion__icontains"]= titulo
#            parametros['titulo__contains']=
        #if fecha:
        #    date = parse_date(fecha)
            
        #    parametros["fecha__gte"]= my_date.combine(date, datetime.time(0, 0)) 
        #    parametros["fecha__lte"]= my_date.combine(date, datetime.time(23, 59)) 
            
        if cat !='0' and cat is not None:
       
            parametros["rubro"]= cat

        
        articulos = articulos.filter(**parametros)
    
   
        
        return articulos.order_by('descripcion',"rubro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["ListaRubros"] =  Rubros.objects.all()
        return context




class Editar(LoginRequiredMixin, IsAdminMixin, UpdateView):   
#class Editar(UpdateView):   
    model         = Articulos 
    template_name = "articulos/editar.html"
    form_class    = ArticuloForm     

    def get_success_url(self):
        return reverse("Articulos:listado")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sucursal"] =  Sucursales.objects.all()
        return context




@is_admin_required()
def Importar(request):  
    data = None
    mi_empresa = request.user.empresa
    
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
                    Rubros.objects.create(descripcion=descripcion,empresa=mi_empresa)        
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
                    Articulos.objects.create(codigo=codigo, descripcion=descripcion,rubro=rubro,precio=precio,empresa=mi_empresa)        
                else:
                    existe.update(descripcion=descripcion,precio=precio)

        #result = Employee.import_data(data_import,dry_run=True,raise_errors=True)
        #if not result.has_errors():
        #    Employee.import_data(dataset,dry_run=False)        
    
          
    contexto = {}
    return render(request, template_name, contexto)




@csrf_exempt
@is_admin_required()
def qr_crear(request):  
    template_name = 'articulos/qr_crear.html' 
    contexto = {}
    sucursales = Sucursales.objects.all()
    contexto["Sucursales"] =  sucursales
    
    if request.method == 'POST' :
       
        parametros = {}
        
        cat      = request.POST.get("rubro")
        print(cat)
        if cat !='0' and cat is not None:
       
            parametros["id"]= cat

        
            sucursales = sucursales.filter(**parametros)
        
    
        
            data = sucursales[0].url
            img = qrcode.make(data)

            buf = BytesIO()		# BytesIO se da cuenta de leer y escribir bytes en la memoria
            img.save(buf)
            image_stream = buf.getvalue()
            response = HttpResponse(image_stream, content_type="image/png")
            return response
        
        

    
    

    return render(request, template_name, contexto)
 
        

@csrf_exempt
@is_admin_required()
def ver_menu(request, pk):
    contexto = {}
    arti = Articulos.objects.filter(id=pk).first()
    menu = not arti.menu
    arti = Articulos.objects.filter(id=pk)
    arti.update(menu=menu)
    return HttpResponseRedirect(reverse("Articulos:listado"))

    #return HttpResponseRedirect(reverse("inicio"))
