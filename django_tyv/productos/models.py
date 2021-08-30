from django.db import models
from categorias.models import Categoria
# Create your models here.


class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=8, decimal_places=2)
    foto=models.ImageField(upload_to='uploads')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock=models.PositiveIntegerField()
