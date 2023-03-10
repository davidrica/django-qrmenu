
from django import forms
from .models import Sucursales 

class SucursalesForm(forms.ModelForm): 
    descripcion= forms.CharField(label="Descripcion", widget=forms.TextInput())
    url        = forms.CharField(label="URL", widget=forms.TextInput()) 
    class Meta:
        model=Sucursales
        fields = '__all__' 
    