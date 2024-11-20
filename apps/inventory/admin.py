from django.contrib import admin
from .models import Inventory, Ingredient, InventoryIngredientOwnership

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'user', 'ingredient_quantity', 'updated_at')
    search_fields = ('user__fname', 'user__lname')
    ordering = ('user',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_id', 'name', 'category')
    search_fields = ('name', 'category')
    ordering = ('name',)

@admin.register(InventoryIngredientOwnership)
class InventoryIngredientOwnershipAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'inventory', 'purchase_date', 'expiry_date', 'freshness')
    list_filter = ('expiry_date',)
