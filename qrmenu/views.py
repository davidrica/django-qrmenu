from django.shortcuts import render,redirect
from django.urls import reverse

from articulos.models import Articulos 
from rubros.models import Rubros
from empresa.models import Empresa
from sucursales.models import Sucursales

def inicio(request):
    template_name = "index.html"
      
    contexto = {
       
    }
    if not request.user.is_authenticated:


        return redirect("login")
    
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
            parametros = {}
            
            parametros["empresa"]= empresa
            #todos los rubros de la empresa
            rubros    = Rubros.objects.filter(**parametros)
            
            parametros["sucursal"]= sucursal

            articulos = Articulos.objects.filter(**parametros)
            #todos los rubros de los articulso
            rubros =Rubros.objects.filter(arti_rubros__in=articulos.values_list('rubro')).distinct()
            #articulos = articulos.objects.filter()
            
            # ===============================
            # query en django utilizando el orm
            #rubros    = Rubros.objects.filter(**parametros)
            #inicio    = Rubros.objects.first()#.filter(empresa=emp.id).first() 
           # print(rubros)
            contexto = {
                'sucursal':suc.descripcion,
                'Articulos': articulos.order_by('descripcion',"rubro"),
                'Rubros':rubros.order_by("descripcion"),
                #'inicio':inicio,
            }
    
            return render(request, template_name, contexto)
    return redirect("Sucursales:listado")

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
