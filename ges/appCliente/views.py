from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Cliente
# Create your views here.
@validarPermisosEcosapp()
def Crear_cliente(request):
    _context ={
        'clientes': Cliente.objects.filter(),
    }
    return render(request, 'crear_cliente.html', context = _context)

def guardar_editar_cliente(request):
    _respuesta = False
    if request.method == 'POST':
        _cliente = Cliente()
        _cliente.nombres = request.POST.get('nombres')
        _cliente.apellidos = request.POST.get('apellidos')
        _cliente.telefono = request.POST.get('telefono')
        _cliente.direccion = request.POST.get('direccion')
        _cliente.save()
        _respuesta = True
    json = { 'accionEjecutada': _respuesta }
    return JsonResponse(json, safe=False)