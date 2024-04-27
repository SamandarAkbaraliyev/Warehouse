from django.db import models
from utils.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Material(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductMaterial(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Warehouse(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.material.name
