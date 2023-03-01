from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Producto
# Create your views here.
@validarPermisosEcosapp()
def Crear_Ver_Producto(request):
    _context ={
        'productos': Producto.objects.filter(registroActivo=True)
    }
    return render(request, 'crear_ver_producto.html', context = _context)

def guardar_editar_producto(request):
    _respuesta = False
    if request.method == 'POST':
        _producto = Producto()
        _producto.nombre = request.POST.get('nombre')
        _producto.precio = request.POST.get('precio')
        _producto.descripcion = request.POST.get('Descripcion')
        _producto.save()
        _respuesta = True
    json = { 'accionEjecutada': _respuesta }
    return JsonResponse(json, safe=False)