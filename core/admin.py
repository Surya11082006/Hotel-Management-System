from django.contrib import admin
from .models import Restaurant, Order, DeliveryAgent

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'phone', 'created_at')
    search_fields = ('name', 'address', 'phone')
    list_filter = ('created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'restaurant', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'restaurant__name')

@admin.register(DeliveryAgent)
class DeliveryAgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'available', 'current_location')
    list_filter = ('available',)
    search_fields = ('user__username', 'phone')
