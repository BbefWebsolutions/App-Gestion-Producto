from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import authenticate, get_user, login as auth_login, logout as auth_logout


# Create your views here.
def login(request):
    if request.method == 'POST':
        data = request.POST
        nombre_usuario, contrasena = data.get('username'), data.get('password')
        usuario = authenticate(username=nombre_usuario, password=contrasena)
        if usuario:
            print('usuario')
            auth_login(request, usuario)
            return redirect('inicio')
        else:
            print('no okta')
            msg = "Usuario y/o contraseña invalidos"
            # messages.error(request, msg)
    _context ={}
    return render(request, 'login.html', context = _context)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
