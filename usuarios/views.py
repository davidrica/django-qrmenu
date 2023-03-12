
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Usuario
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import urllib.request

# class Registro(CreateView):
#     model = Usuario 
#     template_name = "usuarios/registro.html"
#     form_class = UsuarioForm

#     def get_success_url(self):
#         return reverse("login")

def Registro(request):  
    template_name = 'usuarios/registro.html'
    error = False
    msg = False
    formulario = True
    if request.method == 'POST' :
        try: 
            newuser =request.POST.get("newuser")
            correo  =request.POST.get("correo")
            telefono=request.POST.get("telefono")
            if Usuario.objects.filter(username=newuser).exists() or Usuario.objects.filter(telefono=telefono).exists() or Usuario.objects.filter(email=correo).exists():
               msg='El usuario ya se encuentra registrado'
            else:
                newpassword = Usuario.objects.make_random_password()         
                
                user = Usuario.objects.create_user(username=newuser,es_admin=False,email=correo,telefono=telefono,password=newpassword)
                email = EmailMessage("Gracias Por Registrarse"  ,f"{newuser} su contraseña es: {newpassword}."  , to=[correo])
                email.send()
            # msg = 'Controle su casilla de correo ' + correo + " alli tendra la contraseña de ingreso"
                formulario= False
        except Exception as ex:
            error = True
            msg   = ex
        #with urllib.request.urlopen('https://mensajesapp.com.ar/test.php?nTo=543644727579&msj=buenas') as response:
        #    html = response.read()


    contexto = {'msg':msg,'error':error ,'formulario':formulario}
    #message.error(request, 'bla bla bla')
    return render(request, template_name,contexto)
    #return HttpResponseRedirect(reverse ('inicio', kwargs={'msg':FooBar}))

    