from rest_framework import serializers
from .models import OfflineOrder, Order
from users.serializers import RegisterSerializer
from cart.serializers import CartItemsSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    items = CartItemsSerializer(many=True)
    class Meta:
        model = Order
        exclude = ['update']


class OfflineOrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    class Meta:
        model = OfflineOrder
        fields = ['quantity', 'address', 'product_id']