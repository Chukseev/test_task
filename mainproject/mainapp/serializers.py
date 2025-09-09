from rest_framework import serializers
from .models import OrderItem, Product, Order

class AddItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate(self, data):
        try:
            product = Product.objects.get(id=data["product_id"])
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found")

        if product.quantity < data["quantity"]:
            raise serializers.ValidationError("Недостаточно товара на складе")

        data["product"] = product
        return data


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "product_name", "quantity", "price"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'client_name', 'order_date']