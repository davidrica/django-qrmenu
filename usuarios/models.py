from django.db import models
from django.contrib.auth.models import AbstractUser
from empresa.models import Empresa

class Usuario(AbstractUser):
    es_admin  = models.BooleanField(default=False)
    telefono  = models.TextField(max_length=13,default='',blank=True)
    bloqueado = models.BooleanField(default=False)
    empresa   = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True,related_name="usuario_empresa",blank=True)