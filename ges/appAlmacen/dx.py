from django.http import JsonResponse
from .models import Almacen
from appUsuario.user_decorator import validarPermisosEcosapp

@validarPermisosEcosapp()
def jsonAlmacenes(request):
    data = []
    almacenes = Almacen.objects.filter()
    for producto in almacenes:
        json={
            'nombre': producto.nombre,
            'direccion': producto.direccion,
        }
        data.append(json)
    return JsonResponse(data, safe=False)