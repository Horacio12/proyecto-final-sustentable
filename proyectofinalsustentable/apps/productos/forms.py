from django import forms

from . models import Producto

class ProductoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Producto", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre del producto"}))

	class Meta:
		model = Producto
		fields = ["nombre", "precio"]