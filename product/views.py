from rest_framework.response import Response
from .models import Product
from category.models import Category
from users.models import Company
from rest_framework import generics,status
from .serializers import (ProductSerializer,CreateProductSerializer)
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsBoss
from django.shortcuts import get_object_or_404
from utils.pagination import SetPagination


class ListProductView(generics.ListAPIView): 
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer 
    pagination_class = SetPagination
    filterset_fields = ['category','name','company']
    search_fields = ['name','category__title']
    ordering_fields = ['create']  
    ordering = ['-create']


class CreateProductView(generics.CreateAPIView): 
    permission_classes = (IsBoss, )
    serializer_class = CreateProductSerializer
    model = Product

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         category = get_object_or_404(Category, pk=serializer.data.get('category'))
    #         company = get_object_or_404(Company, pk=serializer.data.get('company'))
    #         try:
    #             product = Product(
    #             name=serializer.data.get('name'),
    #             image=request.FILES['image'],
    #             price=serializer.data.get('price'),
    #             category=category,
    #             company=company
    #             )
    #             product.save()
    #         except:
    #             product = Product(
    #             name=serializer.data.get('name'),
    #             price=serializer.data.get('price'),
    #             category=category,
    #             company=company
    #             )
    #             product.save()    
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer



        
      


