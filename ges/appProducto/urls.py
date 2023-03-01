from django.urls import path

from appProducto import views, dx
# from appInicio import dx

urlpatterns = [
    path('crear/ver/producto', views.Crear_Ver_Producto, name='crear_ver_cliente'),
    path('agregar_editar_producto', views.guardar_editar_producto, name='agregar_editar_producto'),
    path('listar_productos', dx.jsonProductos, name='listar_productos'),
]