from product.models import Product
from .models import OfflineOrder, Order
from rest_framework import status,generics
from rest_framework.response import Response
from .serializers import OrderSerializer,OfflineOrderSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.cache import cache
from cart.models import Item
from cart.cart import Cart
from utils.permissions import IsCustomer, IsVisitor
from django.shortcuts import get_object_or_404


def calculateCartPrice(request,order,items):
    price = 0
    for item in items:
        price += item.price * item.quantity
        order.items.add(item)

    order.amount = price
    order.save()  

    cache.delete(f'{request.user}-cart')
    cart = Cart(request)
    cart.clear()


class CreateOrderView(generics.GenericAPIView): 
    permission_classes = [IsCustomer]

    def post(self,request):
        
        cart_id = cache.get(f'{request.user}-cart')
        if cart_id is not None:
            items = Item.objects.filter(cart=cart_id)
            order = Order.objects.create(
                state='p',
                deliverMethod='p',
                paymentMethod='o',
                user=request.user
            )
            #calculate cart price
            calculateCartPrice(request,order,items)   
            return  Response({'message':'create order successfully'},status.HTTP_200_OK)  
        else:
            return Response({'message': 'cart is empty'})         
                   

class ListOrderView(generics.ListAPIView):  
    permission_classes = [IsCustomer]
    serializer_class = OrderSerializer
    def get_queryset(self):
        order = Order.objects.filter(user=self.request.user)
        return order


class RetrieveUpdateDestroyOrderView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


#create order by visitor
class CreateOfflineOrderView(generics.ListCreateAPIView): 
    permission_classes = (IsVisitor, )
    serializer_class = OfflineOrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            product = get_object_or_404(Product, pk=serializer.data.get('product_id'))
            order = OfflineOrder(
            quantity=serializer.data.get('quantity'),
            address=serializer.data.get('address'),
            product_id=product,
            visitor_id=request.user
            )
            order.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
