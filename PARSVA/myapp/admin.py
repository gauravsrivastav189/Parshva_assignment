from django.contrib import admin
from .models import Supplier, PurchaseOrder, Docket


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'description']

@admin.register(Docket)
class DocketAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time', 'num_hours_worked', 'rate_per_hour', 'supplier', 'purchase_order']
