from rest_framework import serializers
from warehouse.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'code']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        quantity = self.context.get('quantity')
        data['quantity'] = quantity
        return data
