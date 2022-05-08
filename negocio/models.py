from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    tamano = models.CharField(max_length=4)
    destacado = models.BooleanField(default=False)
    oferta = models.BooleanField(default=False)
    precio_unitario = models.DecimalField(
        default=0.0,
        decimal_places=2,
        max_digits=6)

    def guardar(self):
        self.save_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
