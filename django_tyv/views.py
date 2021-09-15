# from django.shortcuts import render//comentado para evitar error en test, hasta que se use
from negocio.models import Producto


def inicio(request):
    productos = Producto.objects.all().order_by('-id')

    return render(request,
                  'inicio.html',
                  {'products': productos})
