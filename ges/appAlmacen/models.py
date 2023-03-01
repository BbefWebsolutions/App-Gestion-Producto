from django.db import models
from appProducto.models import Producto

# Create your models here.
class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    registroActivo = models.BooleanField(default=True, verbose_name = '¿Activo?')

    def __str__(self):
        return self.nombre
    
class Existencia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE , null = True, blank = True, default = None, verbose_name = 'Producto')
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE , null = True, blank = True, default = None, verbose_name = 'Almacen')
    cantidad = models.PositiveIntegerField(null = True, blank = True, default = 0, verbose_name = 'Cantidad Producto')
    registroActivo = models.BooleanField(default=True, verbose_name = '¿Activo?')

    def __str__(self):
        return f'{self.producto.nombre} en {self.almacen.nombre}: {self.cantidad}'