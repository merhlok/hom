from django.contrib import admin

from django.contrib import admin
from app.models import Car, Sale, Client

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'price', 'fuel_type')
    list_filter = ('year', 'body_type', 'fuel_type')
    search_fields = ('model',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'client', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
