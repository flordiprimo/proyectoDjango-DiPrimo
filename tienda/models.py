from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)


class Remera(models.Model):
    modelo = models.CharField("Modelo",max_length=30)
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = models.PositiveSmallIntegerField("Talle",choices=TALLES)
    color = models.CharField("Color",max_length=15)
    precio = models.FloatField("Precio $")
    descripcion = models.CharField("Descripción",max_length=200)
    imagen = models.ImageField(upload_to='remeras', null=True, blank=True)

    
class Pantalon(models.Model):
    modelo = models.CharField("Modelo",max_length=30)
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = models.PositiveSmallIntegerField("Talle",choices=TALLES)
    color = models.CharField("Color",max_length=15)
    precio = models.FloatField("Precio $")
    descripcion = models.CharField("Descripción",max_length=200)
    imagen = models.ImageField(upload_to='pantalones', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Pantalon'
        verbose_name_plural = 'Pantalones'

class Camisa(models.Model):
    modelo = models.CharField("Modelo",max_length=30)
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = models.PositiveSmallIntegerField("Talle",choices=TALLES)
    color = models.CharField("Color",max_length=15)
    precio = models.FloatField("Precio $")
    descripcion = models.CharField("Descripción",max_length=200)
    imagen = models.ImageField(upload_to='camisas', null=True, blank=True)
