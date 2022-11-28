from rest_framework import serializers
from .models import Order, OrderItem
from book.serializers import BookSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):    
    book = BookSerializer()
    class Meta:
        model = OrderItem
        fields = (
            "book",
            "isbn",
            "price",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "state",
            "city",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrderItem
        fields = (
            "book",
            "isbn",
            "price",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "state",
            "city",
            "phone",
            "stripe_token",
            "items",
        )  
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)  
        return order