from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Almacen
from .models import Existencia
from appProducto.models import Producto
# Create your views here.
@validarPermisosEcosapp()
def Crear_Ver_Almacenes(request):
    _context ={
        'Almacenes': Almacen.objects.filter(registroActivo=True)
    }
    return render(request, 'crear_ver_almacen.html', context = _context)

def guardar_editar_almacenes(request):
    _respuesta = False
    if request.method == 'POST':
        _almacen = Almacen()
        _almacen.nombre = request.POST.get('nombre')
        _almacen.direccion = request.POST.get('direccion')
        _almacen.save()
        _respuesta = True
    json = { 'accionEjecutada': _respuesta }
    return JsonResponse(json, safe=False)

def guardar_editar_producto_almacen(request):
    _respuesta = False
    if request.method == 'POST':
        _existencia = Existencia()
        _existencia.producto = Producto.objects.get(id=int(request.POST.get('id_prod')))
        _existencia.almacen = Almacen.objects.get(id=int(request.POST.get('almacen')))
        _existencia.cantidad = request.POST.get('cantidad')
        _existencia.save()
        _respuesta = True
    json = { 'accionEjecutada': _respuesta }
    return JsonResponse(json, safe=False)