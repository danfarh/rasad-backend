from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ['company_id','category']
    list_display = ('id', 'name', 'price', 'category', 'company')                 


