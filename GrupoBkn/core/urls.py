from django.urls import path
from .views import index, administracion, bodega, boleta, carrito, ficha, historial_ventas, ingresar, menu, mis_compras, misdatos, nosotros, registro, ropa, usuarios, mantenedor_prod, producto_ficha, productos


urlpatterns = [
    path('index', index, name="index"),
    path('administracion', administracion, name='administracion'),
    path('bodega', bodega, name='bodega'),
    path('boleta', boleta, name='boleta'),
    path('carrito', carrito, name='carrito'),
    path('ficha', ficha, name='ficha'),
    path('historial_ventas', historial_ventas, name='historial_ventas'),
    path('ingresar', ingresar, name='ingresar'),
    path('menu', menu, name='menu'),
    path('mis_compras', mis_compras, name='mis_compras'),
    path('misdatos', misdatos, name='misdatos'),
    path('nosotros', nosotros, name='nosotros'),
    path('registro', registro, name='registro'),
    path('ropa', ropa, name='ropa'),
    path('usuarios', usuarios, name='usuarios'),
    path('mantenedor_prod', mantenedor_prod, name="mantenedor_prod"),
    path('productos',productos, name='productos'),
    path('productos/<action>/<id>', producto_ficha, name="producto_ficha"),
    
]

