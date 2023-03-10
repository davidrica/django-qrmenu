from django.urls import path

from . import views

app_name="Usuarios"

urlpatterns = [
   path('registro/', views.Registro, name="registro"),
]