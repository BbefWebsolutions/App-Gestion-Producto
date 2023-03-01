from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Almacen
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