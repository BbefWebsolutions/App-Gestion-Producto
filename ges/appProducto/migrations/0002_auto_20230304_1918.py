# Generated by Django 3.0.6 on 2023-03-04 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProducto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=10, null=True, verbose_name='Precio Producto'),
        ),
    ]
