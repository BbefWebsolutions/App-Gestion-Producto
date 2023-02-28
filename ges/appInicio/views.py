from django.shortcuts import render
from appUsuario.user_decorator import validarPermisosEcosapp

# Create your views here.
@validarPermisosEcosapp()
def inicio(request):
    _context ={}
    return render(request, 'dashboard.html', context = _context)
