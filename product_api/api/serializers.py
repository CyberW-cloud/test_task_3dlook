from rest_framework import serializers
from product_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.logo = validated_data.get("logo", instance.logo)
        instance.rotate_duration = validated_data.get("rotate_duration", instance.rotate_duration)
        instance.save()
        return instance
