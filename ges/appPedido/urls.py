from django.urls import path

from appPedido import views, dx
# from appInicio import dx

urlpatterns = [
    path('crear/ver/pedido', views.Crear_Ver_Pedido, name='crear_ver_pedido'),
    path('guardar_editar_pedido', views.guardar_editar_pedido, name='guardar_editar_pedido'),
    path('listar_pedidos', dx.jsonPedidos, name='listar_pedidos'),
]