from django.shortcuts import render
from django.urls import reverse

from articulos.models import Articulos 
from rubros.models import Rubros

def inicio(request):
    template_name = "index.html"
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

def inicio2(request):
    template_name = "modelo2.html"
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
