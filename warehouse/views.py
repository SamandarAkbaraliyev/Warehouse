from django.shortcuts import render
from rest_framework.views import APIView
from warehouse.models import Product, ProductMaterial
from rest_framework.response import Response
from warehouse.serializers import ProductSerializer
from django.db.models import Subquery


class ProductMaterialAPIView(APIView):
    def post(self, request, *args, **kwargs):
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        products = Product.objects.filter(name=product).annotate(
            product_materials=Subquery(ProductMaterial.objects.filter()))

        data = ProductSerializer(products, many=True, context={'quantity': quantity})
        return Response(data.data, status=200)
