from django.db import models
from appAlmacen.models import Existencia
from appCliente.models import Cliente
# Create your models here.
class Movimiento(models.Model):
    existencia = models.ForeignKey(Existencia, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.tipo} de {self.cantidad} a {self.existencia}'
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente}'
    
# ? Necesidad del modelo compra
# class Compra(models.Model):
#     proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_entrega = models.DateField()
#     estado = models.CharField(max_length=20, default='pendiente')

#     def __str__(self):
#         return f'Compra {self.id} a {self.proveedor}'