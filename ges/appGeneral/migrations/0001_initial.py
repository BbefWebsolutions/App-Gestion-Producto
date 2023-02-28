# Generated by Django 3.0.6 on 2023-02-27 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCliente', '0001_initial'),
        ('appAlmacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha Creacion')),
                ('fecha_entrega', models.DateField(blank=True, default=None, null=True, verbose_name='Fecha Entrega')),
                ('estado', models.CharField(blank=True, default='pendiente', max_length=20, null=True, verbose_name='Estado')),
                ('cliente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appCliente.Cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha Movimiento')),
                ('cantidad', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Cantidad')),
                ('tipo', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Tipo Movimiento')),
                ('existencia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAlmacen.Existencia', verbose_name='Existencia')),
            ],
        ),
    ]
