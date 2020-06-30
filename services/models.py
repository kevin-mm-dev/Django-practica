from django.db import models

class Products(models.Model):
    name = models.CharField('NOMBRE/DESC PRODUCTO', max_length=60)
    category = models.CharField('Categoria', max_length=20)
    ubication = models.CharField('Ubicacion', max_length=60)
    lote = models.CharField('Lote', max_length=20)