from django.urls import path

from appAlmacen import views, dx
# from appInicio import dx

urlpatterns = [
    path('crear/ver/almacen', views.Crear_Ver_Almacenes, name='crear_ver_almacen'),
    path('guardar_editar_almacenes', views.guardar_editar_almacenes, name='guardar_editar_almacenes'),
    path('guardar_editar_producto_almacen', views.guardar_editar_producto_almacen, name='guardar_editar_producto_almacen'),
    path('listar_almacenes', dx.jsonAlmacenes, name='listar_almacenes'),
]