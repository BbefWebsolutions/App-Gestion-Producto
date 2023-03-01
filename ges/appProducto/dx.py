from django.http import JsonResponse
from appProducto.models import Producto
from appUsuario.user_decorator import validarPermisosEcosapp

@validarPermisosEcosapp()
def jsonProductos(request):
    data = []
    productos = Producto.objects.filter()
    for producto in productos:
        json={
            'nombre': producto.nombre,
            'precio': producto.precio,
            'descripcion': producto.descripcion,
        }
        data.append(json)
    return JsonResponse(data, safe=False)