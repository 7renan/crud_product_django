from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.FloatField('Preço')
    category = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.name
