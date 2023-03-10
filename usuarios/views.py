
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
    msg='' 
    if request.method == 'POST' :
        try:

            newpassword = Usuario.objects.make_random_password()         
            newuser =request.POST.get("newuser")
            correo  =request.POST.get("correo")
            telefono=request.POST.get("telefono")
            
            user = Usuario.objects.create_user(username=newuser,es_admin=False,email=correo,telefono=telefono,password=newpassword)

            email = EmailMessage('Subject', newpassword, to=[correo])
            email.send()
            msg = 'Controle su casilla de correo ' + correo + " alli tendra la contraseña de ingreso"
        except Exception as ex:
            msg= ex
        #with urllib.request.urlopen('https://mensajesapp.com.ar/test.php?nTo=543644727579&msj=buenas') as response:
        #    html = response.read()


        

    contexto = {'msg':msg}
    #message.error(request, 'bla bla bla')
    return render(request, 'login.html',contexto)
    #return HttpResponseRedirect(reverse ('inicio', kwargs={'msg':FooBar}))

    