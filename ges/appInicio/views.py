from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp
from appCliente.models import Cliente
from appProducto.models import Producto
# Create your views here.
@validarPermisosEcosapp()
def inicio(request):
    _context ={
        'clientes_total': Cliente.objects.filter(registroActivo=True).count()
    }
    return render(request, 'dashboard.html', context = _context)
