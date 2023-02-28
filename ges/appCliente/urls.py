from django.urls import path

from appCliente import views, dx
# from appInicio import dx

urlpatterns = [
    path('crear/cliente', views.Crear_cliente, name='crear_cliente'),
    path('agregar_editar_cliente', views.guardar_editar_cliente, name='agregar_editar_cliente'),
    path('listar_clientes', dx.jsonClientes, name='listar_clientes'),
]