from django import forms
from .models import Categoria, Producto, Venta


class CargaCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class CargaProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'categoria',
            'nombre',
            'marca',
            'tamano',
            'principal',
            'destacado',
            'precio_unitario'
            ]


class CargaVenta(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['item', 'cantidad', 'fecha']
