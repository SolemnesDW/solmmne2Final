from __future__ import unicode_literals
from django.db import models


clasificacion_producto = [(i,i) for i in range(6)]


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True,null=True)
    banner = models.ImageField(upload_to='images/banner_categorias',blank=True,null=True)
    orden_clasificacion = models.IntegerField(default=0)
    estado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    banner = models.ImageField(upload_to='images/banner_marcas',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen_producto = models.ImageField(upload_to='images/productos',blank=True,null=True)
    marca = models.ForeignKey(Marca)
    descripcion = models.TextField()    
    sku = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    clasificacion = models.IntegerField(choices=clasificacion_producto)
    categoria = models.ForeignKey(Categoria)
    estado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Slider(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='images/sliders',blank=True,null=True)
    descripcion = models.TextField()
    orden_clasificacion = models.IntegerField(default=0)
    estado = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


