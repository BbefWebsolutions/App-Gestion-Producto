from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.signals import user_logged_in
from django.db.models import Q
from django.utils import timezone

def validarPermisosEcosapp():
    def wrap_view(view_function):
            """ función que recibe como parametro la función view """

            def validarReglas(request,*args, **kwargs):
                usuario_cliente = not any([request.user.is_staff, request.user.is_superuser])
                if request.user.is_authenticated: # (1)
                    usuario = request.user.usuario 

                        
                else:
                    return redirect('login')