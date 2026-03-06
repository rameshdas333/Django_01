from rest_framework import serializers
from .models import Product,Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['quantity:']


class ProductSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
# class InventorySerializers(serializers.ModelSerializer):
#       quantity = serializers.CharField()

# class ProductSerializer(serializers.ModelSerializer):
#     inventory = InventorySerializer(read_only=True)

#     class Meta:
#         model = Product
#         fields = '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['quantity info:'] = InventorySerializer(instance).data
        return data