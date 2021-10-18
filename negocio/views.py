from django.shortcuts import redirect, render
from .forms import CargaProducto, CargaCategoria, CargaVenta
from django_tyv.views import inicio
from django.contrib.auth.models import Group

def cargaCategoria(request):
    form= CargaCategoria(request.POST or None)
    context={'form':form}
    if form.is_valid():
        categoria=form.save(commit=False)
        # Acá se puede hacer alguna modificacion a los datos ingresados en el form
        categoria.save()
        return redirect(cargaCategoria)
    return render(request,'cargarCategoria.html',context)

def cargarProducto(request):
    form= CargaProducto(request.POST or None)
    context={'form':form}
    if form.is_valid():
        producto=form.save(commit=False)
        # Acá se puede hacer alguna modificacion a los datos ingresados en el form
        producto.save()
        return redirect(cargarProducto)
    return render(request,'cargarProducto.html',context)

def cargaVenta(request):
    form=CargaVenta(request.POST or None)
    context={'form':form}
    if form.is_valid():
        venta=form.save(commit=False)
        precio=venta.item.precio_unitario
        venta.precio=precio
        venta.monto=venta.precio*venta.cantidad
        venta.save()
        return redirect(cargaVenta)
    return render(request, 'cargarVenta.html',context)

def administracion(request):
    return render(request, 'administracion.html')

def logueado(request):
    programadores = Group.objects.get(name="Programadores").user_set.all()
    propietarios= Group.objects.get(name="Propietarios").user_set.all()
    clientes= Group.objects.get(name="Clientes").user_set.all()
    usuario=request.user
    print(usuario)
    print(programadores)
    if usuario in programadores or usuario in propietarios:
        return redirect(administracion)
    elif usuario in clientes:
        return redirect(inicio)
    else:
        return redirect('accounts/login/')