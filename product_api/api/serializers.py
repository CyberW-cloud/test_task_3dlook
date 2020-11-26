from rest_framework import serializers
from product_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'description', 'created', 'updated', 'logo', 'rotate_duration']
