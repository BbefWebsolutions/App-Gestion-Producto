from django.http import JsonResponse
from .models import Pedido
from appUsuario.user_decorator import validarPermisosEcosapp

@validarPermisosEcosapp()
def jsonPedidos(request):
    data = []
    pedidos = Pedido.objects.filter(registroActivo=True)
    for pedido in pedidos:
        json={
            'cliente':   pedido.cliente.nombres + ' ' + pedido.cliente.apellidos,
            'movimiento': f'{pedido.movimiento.tipo} de {pedido.movimiento.cantidad} {pedido.movimiento.existencia.producto.nombre} a {pedido.cliente.nombres} {pedido.cliente.apellidos}',
            'ganancia': '$'+str(pedido.movimiento.cantidad*pedido.movimiento.existencia.producto.precio)
        }
        data.append(json)
    return JsonResponse(data, safe=False)