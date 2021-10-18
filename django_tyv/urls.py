from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from negocio import views as viewsNegocio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),
    path('carga_producto/',viewsNegocio.cargarProducto),
    path('carga_categoria/',viewsNegocio.cargaCategoria),
    path('carga_venta/',viewsNegocio.cargaVenta),
    path('administracion/',viewsNegocio.administracion),
    path('logueado',viewsNegocio.logueado),
    path('accounts/', include('django.contrib.auth.urls')),
]
