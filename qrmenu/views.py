from django.shortcuts import render,redirect
from django.urls import reverse

from articulos.models import Articulos 
from rubros.models import Rubros
from empresa.models import Empresa
from sucursales.models import Sucursales
from django.core.management.utils import get_random_secret_key

def inicio(request):
    

    # generating and printing the SECRET_KEY
    print(get_random_secret_key())

    template_name   = "index.html"
    suc             =  Sucursales.objects.all() 
    contexto        = {
        'sucursales': suc,
       
    }
    #if not request.user.is_authenticated:


    #    return redirect("login")
    
    return render(request, template_name, contexto)





# def inicio(request):
#     template_name = "index.html"
#     articulos = Articulos.objects.all()
#     # ===============================
#     # query en django utilizando el orm
#     rubros    = Rubros.objects.all()
#     inicio    = Rubros.objects.first()  

#     contexto = {
#         'Articulos': articulos.order_by('descripcion',"rubro"),
#         'Rubros':rubros.order_by("descripcion"),
#         'inicio':inicio,
#     }

#     return render(request, template_name, contexto)

def inicio2(request,empresa,sucursal):

    template_name = "modelo2.html"
    if Empresa.objects.filter(id=empresa).exists():
        emp =   Empresa.objects.get(id=empresa)
        if Sucursales.objects.filter(id=sucursal).exists():
            suc = Sucursales.objects.get(id=sucursal)
            
            if suc.activa:
                parametros = {}
                
                parametros["empresa"]  = empresa
                
                parametros["sucursal"] = sucursal

                articulos = Articulos.objects.filter(**parametros)

                ids = articulos.order_by('rubro').values_list('rubro').distinct()

                rubros = Rubros.objects.filter(id__in=ids)

                contexto = {
                    'sucursal':suc.descripcion,
                    'Articulos': articulos.order_by('rubro','descripcion'),
                    'Rubros':rubros.order_by("descripcion"),
                    #'inicio':inicio,
                }

                return render(request, template_name, contexto)
    return redirect("inicio")

def inicio3(request):
    template_name = "modelo3.html"
    articulos = Articulos.objects.all()
    # ===============================
    # query en django utilizando el orm
    rubros    = Rubros.objects.all()
    inicio    = Rubros.objects.first()  

    contexto = {
        'Articulos': articulos.order_by('descripcion',"rubro"),
        'Rubros':rubros.order_by("descripcion"),
        'inicio':inicio,
    }

    return render(request, template_name, contexto)
