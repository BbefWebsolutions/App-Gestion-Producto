from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Pedido, Movimiento
from appAlmacen.models import Almacen, Existencia
from appCliente.models import Cliente
import datetime
# Create your views here.
@validarPermisosEcosapp()
def Crear_Ver_Pedido(request):
    _context ={
        'pedidos': Pedido.objects.filter(registroActivo=True),
        'stocks': Existencia.objects.filter(registroActivo=True),
        'clientes': Cliente.objects.filter(registroActivo=True),
    }
    return render(request, 'crear_ver_pedido.html', context = _context)

def guardar_editar_pedido(request):
    _respuesta = False
    if request.method == 'POST':
        # Creacion del movimiento del producto
        _movimiento = Movimiento()
        _movimiento.existencia = Existencia.objects.get(id=int(request.POST.get('existencia')))
        _movimiento.cantidad = request.POST.get('cantidad')
        _movimiento.tipo = 'Pedido'
        _movimiento.save()

        # Restar cantidad a la existencia
        _movimiento.existencia.cantidad = (int(_movimiento.existencia.cantidad))-int(request.POST.get('cantidad'))
        _movimiento.existencia.save()

        # Creacion del pedido
        _pedido = Pedido()
        _pedido.cliente = Cliente.objects.get(id=int(request.POST.get('cliente')))
        _pedido.movimiento = _movimiento
        _pedido.fecha_entrega = datetime.date.today()
        _pedido.save()
        _respuesta = True
    json = { 'accionEjecutada': _respuesta }
    return JsonResponse(json, safe=False)