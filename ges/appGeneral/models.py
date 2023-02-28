from django.db import models
from appAlmacen.models import Existencia
from appCliente.models import Cliente
# Create your models here.
class Movimiento(models.Model):
    existencia = models.ForeignKey(Existencia, on_delete=models.CASCADE, null = True, blank = True, default = None, verbose_name = 'Existencia')
    fecha = models.DateTimeField(auto_now_add=True, null = True, blank = True, verbose_name = 'Fecha Movimiento')
    cantidad = models.PositiveIntegerField(null = True, blank = True, default = None, verbose_name = 'Cantidad')
    tipo = models.CharField(max_length=10, null = True, blank = True, default = None, verbose_name = 'Tipo Movimiento')

    def __str__(self):
        return f'{self.tipo} de {self.cantidad} a {self.existencia}'
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null = True, blank = True, default = None, verbose_name = 'Cliente')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank = True, verbose_name = 'Fecha Creacion')
    fecha_entrega = models.DateField(null = True, blank = True, default = None, verbose_name = 'Fecha Entrega')
    estado = models.CharField(max_length=20, default='pendiente', null = True, blank = True, verbose_name = 'Estado')

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