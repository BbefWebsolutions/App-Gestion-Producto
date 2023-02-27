from django.db import models

# Create your models here.

# ? Necesidad del modelo Proveedor
# class Proveedor(models.Model):
#     nombre = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=255)
#     telefono = models.CharField(max_length=20)

#     def __str__(self):
#         return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre