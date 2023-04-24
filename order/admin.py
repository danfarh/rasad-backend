from django.contrib import admin
from .models import Order,OfflineOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('state','amount')
    search_fields = ('state','amount')
    list_display = (
        'state',
        'amount',
        'deliverMethod',
        'paymentMethod',
        'create',
        'update'
    )

@admin.register(OfflineOrder)
class OfflineOrderAdmin(admin.ModelAdmin):
    pass