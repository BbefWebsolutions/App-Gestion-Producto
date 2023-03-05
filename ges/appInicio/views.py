from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from appCliente.models import Cliente
from appProducto.models import Producto
from appPedido.models import Pedido
# Create your views here.
@validarPermisosEcosapp()
def inicio(request):
    fechas = []
    ganancia=[]
    ganancia_total = 0
    pedidos =  Pedido.objects.filter(registroActivo=True).order_by('fecha_entrega')
    for pedido in pedidos:
        ganancia_total += pedido.movimiento.cantidad*pedido.movimiento.existencia.producto.precio
        if not str(pedido.fecha_entrega) in fechas:
            fechas.append(str(pedido.fecha_entrega))
            ganancia.append(int(pedido.movimiento.cantidad*pedido.movimiento.existencia.producto.precio))
        else:
            index = fechas.index(str(pedido.fecha_entrega))
            print(index)
            ganancia[index] += int(pedido.movimiento.cantidad*pedido.movimiento.existencia.producto.precio)
    print(fechas)
    print(ganancia)

    _context ={
        'clientes_total': Cliente.objects.filter(registroActivo=True).count(),
        'pedidos_total': Pedido.objects.filter(registroActivo=True).count(),
        'fechas': fechas,
        'ganancia': ganancia,
        'ganancia_total': ganancia_total,
    }
    return render(request, 'dashboard.html', context = _context)
