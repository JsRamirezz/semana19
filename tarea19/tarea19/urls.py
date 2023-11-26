from django.contrib import admin
from django.urls import path
from app1 import views as ap1v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ap1v.index,name="home"),
    path('error/',ap1v.acceso_denegado,name="acceso_denegado"),
    path('registro/',ap1v.reg_user),
    path('login/',ap1v.iniciar_sesion,name="login"),
    path('logout/',ap1v.cerrar_sesion,name="logout"),
    path('registrar_proveedor/', ap1v.registrar_proveedor, name='registrar_proveedor'),
    path('mostrar_proveedores/',ap1v.mostrar_proveedores, name='mostrar_proveedores'),
    path('registrar_producto/', ap1v.registrar_producto, name='registrar_producto'),
    path('mostrar_productos/', ap1v.mostrar_productos, name='mostrar_productos'),
]
