from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=100, null = True, blank = True, default = None, verbose_name = 'Nombres del Cliente')
    apellidos = models.CharField(max_length=100, null = True, blank = True, default = None, verbose_name = 'Apellidos del Cliente')
    direccion = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Direccion Cliente')
    telefono = models.CharField(max_length=20, null = True, blank = True, default = None, verbose_name = 'Telefono cliente')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos