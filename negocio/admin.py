from negocio.models import Categoria, Producto, Venta
from django.contrib import admin


class ProductoAdmin(admin.ModelAdmin):
    list_display=[
        'marca', 
        'nombre', 
        'tamano', 
        'principal', 
        'destacado', 
        'precio_unitario', 
        'categoria'
        ]
    list_editable=[
        'nombre', 
        'tamano', 
        'principal', 
        'destacado', 
        'precio_unitario', 
        'categoria'
        ]


admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
