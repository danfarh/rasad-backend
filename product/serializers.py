from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer
from users.serializers import CompanySerializer
from category.models import Category
from users.models import Company


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    company = CompanySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'category', 'company']  


class CreateProductSerializer(serializers.ModelSerializer):
    category = serializers.IntegerField(write_only=True)
    company = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'category', 'company']  

    @transaction.atomic
    def create(self, validated_data):
        category = validated_data.pop('category')
        company = validated_data.pop('company')
        product = Product(**validated_data)
        product.image = validated_data.get('image')
        product.category = get_object_or_404(Category, pk=category)
        product.company = get_object_or_404(Company, pk=company)
        product.save()
        return product

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance    