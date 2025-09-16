from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Order, OrderItem, Product
from .serializers import AddItemSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer


class AddItemToOrderView(APIView):
    serializer_class = OrderSerializer

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = AddItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data["product"]
        qty = serializer.validated_data["quantity"]

        with transaction.atomic():
            product.refresh_from_db()
            if product.quantity < qty:
                return Response({"detail": "Недостаточно товара на складе"}, status=409)

            product.quantity -= qty
            product.save()

            order_item, created = OrderItem.objects.get_or_create(
                order=order,
                product=product,
                defaults={"quantity": qty, "price": product.price},
            )
            if not created:
                order_item.quantity += qty
                order_item.save()

        return Response(OrderItemSerializer(order_item).data, status=200)

    def get(self, request, order_id):

        order = get_object_or_404(Order, id=order_id)
        items = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data, status=200)

class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)