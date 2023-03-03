from django import forms
from .models import Articulos 

class DatasetForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__' 



 
class ArticuloForm(forms.ModelForm):
    codigo= forms.CharField(label="Codigo", widget=forms.NumberInput())
    descripcion= forms.CharField(label="Descripcion", widget=forms.TextInput())
    #precio= forms.CharField(label="Precio", widget=forms.DecimalField(is_hidden=False))
   


    class Meta:
        model=Articulos
        fields = '__all__' 
    
    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un numero positivo")
        return precio 