from django.contrib import admin
from warehouse.models import Product, Material, ProductMaterial, Warehouse

admin.site.register([Product, Material, ProductMaterial, Warehouse])
