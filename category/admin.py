from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('status','type')
    search_fields = ('title','status')
    list_display = (
        'id',
        'title',
        'parent',
        'slug',
        'status',
        'type'
    )
