from cart.models import Item
from django.shortcuts import HttpResponse,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.cart import Cart
from product.models import Product
from django.core.cache import cache
from rest_framework import generics,status
from .serializers import (CartSerializer,CartItemsSerializer,AddToCartSerializer)
from utils.permissions import IsCustomer
   

class AddToCartView(generics.GenericAPIView): 
    permission_classes = (IsCustomer, )
    serializer_class = AddToCartSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.GET)
        if serializer.is_valid():
            product_id = serializer.data.get('product_id')
            quantity = serializer.data.get('quantity')
            product = get_object_or_404(Product,id=product_id)
            cart = Cart(request)
            cart.add(product, product.price, quantity)
            cache.set(f'{request.user}-cart',str(cart.get_cart_id()),timeout=20*24*3600) #20 days

            return Response({'message':'added to cart successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetCartView(generics.GenericAPIView): 
    permission_classes = (IsCustomer, )

    def get(self, request):
        cart_id = cache.get(f'{request.user}-cart')
        if cart_id is not None:
            items = Item.objects.filter(cart=cart_id)
            serializer = CartItemsSerializer(items,many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'data': []})         


class GetTotalCartPriceView(generics.GenericAPIView): 
    permission_classes = (IsCustomer, )

    def get(self, request):
        cart_id = cache.get(f'{request.user}-cart')
        print(cart_id)
        if cart_id is not None:
            price = 0
            items = Item.objects.filter(cart=cart_id)
            for item in items:
                price += item.price * item.quantity   
            return Response({'price': price}, status=status.HTTP_200_OK)    
        return Response({'price': 0})    

         
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponse('removed from cart successfully')
        

     
  
    