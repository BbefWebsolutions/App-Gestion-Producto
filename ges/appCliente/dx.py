from django.http import JsonResponse
from appCliente.models import Cliente
from appUsuario.user_decorator import validarPermisosEcosapp

@validarPermisosEcosapp()
def jsonClientes(request):
    data = []
    clientes = Cliente.objects.filter()
    for cliente in clientes:
        json={
            'nombres': cliente.nombres,
            'apellidos': cliente.apellidos,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
        }
        data.append(json)
    return JsonResponse(data, safe=False)